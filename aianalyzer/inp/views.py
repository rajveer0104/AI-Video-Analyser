from django.shortcuts import render, redirect
from .forms import MediaUploadForm
from pytubefix import YouTube
from moviepy import VideoFileClip
from .models import Transcript
from faster_whisper import WhisperModel
from rag.embedding import create_embeddings
from django.contrib.auth.decorators import login_required
import os
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

    result = None

    if request.method == "POST":

        form = MediaUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            youtube_url = form.cleaned_data.get("youtube_url")
            video_file = form.cleaned_data.get("video_file")
            audio_file = form.cleaned_data.get("audio_file")

            # -------------------------
            # YouTube Video
            # -------------------------

            if youtube_url:

                try:

                    yt = YouTube(youtube_url)

                    video_stream = yt.streams.get_highest_resolution()

                    downloaded_path = video_stream.download(
                        output_path="media/videos"
                    )

                    filename = os.path.basename(downloaded_path)

                    relative_video_path = f"videos/{filename}"

                    video = VideoFileClip(downloaded_path)

                    audio = video.audio

                    audio_path = "downloads/audio1.wav"

                    audio.write_audiofile(audio_path)

                    audio.close()
                    video.close()

                    model = get_model()

                    segments, info = model.transcribe(
                        audio_path,
                        beam_size=1
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
                        title=yt.title,
                        transcript=transcript_text,
                        segments=transcript_segments,
                        video_path=relative_video_path,
                        youtube_url=youtube_url
                    )
                    from rag.embedding import create_embeddings

                    create_embeddings(transcript.id)

                    if os.path.exists(audio_path):
                        os.remove(audio_path)

                    return redirect(
                        "analysis:analysis",
                        transcript_id=transcript.id
                    )

                except Exception as e:

                    result = f"Error: {str(e)}"
            # -------------------------
            # Uploaded Video
            # -------------------------

            elif video_file:

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
                    from rag.embedding import create_embeddings

                    create_embeddings(transcript.id)

                    if os.path.exists(audio_path):
                        os.remove(audio_path)

                    return redirect(
                        "analysis:analysis",
                        transcript_id=transcript.id
                    )

                except Exception as e:

                    result = f"Error: {str(e)}"

            # -------------------------
            # Uploaded Audio
            # -------------------------

            elif audio_file:

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
                        title=audio_file.name,
                        transcript=transcript_text,
                        segments=transcript_segments,
                        video_path=None,
                        youtube_url=None
                    )
                    from rag.embedding import create_embeddings

                    create_embeddings(transcript.id)

                    if os.path.exists(audio_path):
                        os.remove(audio_path)

                    return redirect(
                        "analysis:analysis",
                        transcript_id=transcript.id
                    )

                except Exception as e:

                    result = f"Error: {str(e)}"

    else:

        form = MediaUploadForm()

    context = {
        "form": form,
        "result": result
    }

    return render(
        request,
        "inp/home.html",
        context
    )