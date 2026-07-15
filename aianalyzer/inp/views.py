from django.shortcuts import render, redirect
from .forms import MediaUploadForm
from moviepy import VideoFileClip
from .models import Transcript
from .transcript_api import get_transcript
from faster_whisper import WhisperModel
from django.contrib.auth.decorators import login_required
import os
from rag.embedding import create_embeddings
import uuid

os.makedirs("downloads", exist_ok=True)
os.makedirs("media/videos", exist_ok=True)

# -------------------------------
# Faster Whisper Model (Lazy Load)
# -------------------------------

model = None


def get_model():
    global model

    if model is None:
        model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    return model


def landing(request):
    return render(request, "inp/land.html")


@login_required
def home(request):

    form = MediaUploadForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():

        youtube_url = form.cleaned_data.get("youtube_url")
        video_file = form.cleaned_data.get("video_file")
        audio_file = form.cleaned_data.get("audio_file")

        if youtube_url:
            return process_youtube(request,form, youtube_url)

        elif video_file:
            return process_video(video_file)

        elif audio_file:
            return process_audio(audio_file)

    return render(
        request,
        "inp/home.html",
        {
            "form": form
        }
    )

def process_youtube(request,form, youtube_url):

    try:

        data = get_transcript(youtube_url)

        print(data.keys())      # TEMPORARY

        title = data.get("title", "YouTube Video")
        print("Transcript language:", data["lang"])
        print("Available languages:", data["availableLangs"])

        transcript_text = ""

        transcript_segments = []

        for item in data["content"]:

            transcript_text += item["text"] + " "

            transcript_segments.append({
                "id": len(transcript_segments),
                "start": item["offset"] / 1000,
                "end": (item["offset"] + item["duration"]) / 1000,
                "text": item["text"]
            })

        transcript = Transcript.objects.create(
            title=title,
            transcript=transcript_text,
            segments=transcript_segments,
            youtube_url=youtube_url
        )

        create_embeddings(transcript.id)

        return redirect(
            "analysis:analysis",
            transcript_id=transcript.id
        )

    except Exception as e:

        print(e)

        form.add_error(
            "youtube_url",
            str(e)
        )

        return render(
            request,
            "inp/home.html",
            {
                "form": form
            }
        )
    
def process_video(video_file):

    try:

        extension = os.path.splitext(video_file.name)[1]

        filename = f"{uuid.uuid4()}{extension}"

        relative_video_path = f"videos/{filename}"

        absolute_video_path = os.path.join(
            "media",
            relative_video_path
        )

        with open(absolute_video_path, "wb+") as destination:
            for chunk in video_file.chunks():
                destination.write(chunk)

        video = VideoFileClip(absolute_video_path)

        audio = video.audio

        audio_path = "downloads/uploaded_audio.wav"

        audio.write_audiofile(audio_path)

        audio.close()
        video.close()

        model = get_model()

        segments, info = model.transcribe(
            audio_path,
            beam_size=5
        )

        transcript_text = ""

        transcript_segments = []

        for segment in segments:

            transcript_text += segment.text + " "

            transcript_segments.append({
                "id": len(transcript_segments),
                "start": segment.start,
                "end": segment.end,
                "text": segment.text
            })

        transcript = Transcript.objects.create(
            title=video_file.name,
            transcript=transcript_text,
            segments=transcript_segments,
            video_path=relative_video_path
        )

        create_embeddings(transcript.id)

        if os.path.exists(audio_path):
            os.remove(audio_path)

        return redirect(
            "analysis:analysis",
            transcript_id=transcript.id
        )

    except Exception:

        import traceback
        traceback.print_exc()
        raise
def process_audio(audio_file):

    try:

        audio_path = os.path.join(
            "downloads",
            audio_file.name
        )

        with open(audio_path, "wb+") as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)

        model = get_model()

        segments, info = model.transcribe(
            audio_path,
            beam_size=5,
            language="en"
        )

        transcript_text = ""

        transcript_segments = []

        for segment in segments:

            transcript_text += segment.text + " "

            transcript_segments.append({
                "id": len(transcript_segments),
                "start": segment.start,
                "end": segment.end,
                "text": segment.text
            })

        transcript = Transcript.objects.create(
            title=audio_file.name,
            transcript=transcript_text,
            segments=transcript_segments,
            video_path=None,
            youtube_url=None
        )

        create_embeddings(transcript.id)

        if os.path.exists(audio_path):
            os.remove(audio_path)

        return redirect(
            "analysis:analysis",
            transcript_id=transcript.id
        )

    except Exception:

        import traceback
        traceback.print_exc()
        raise