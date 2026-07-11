from django.shortcuts import render, redirect
from .forms import MediaUploadForm
from pytubefix import YouTube
from moviepy import VideoFileClip
from .models import Transcript
import whisper
from rag.embedding import create_embeddings
from django.contrib.auth.decorators import login_required
import os
import uuid

os.makedirs("downloads", exist_ok=True)
os.makedirs("media/videos", exist_ok=True)

model = whisper.load_model("base")


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

                    downloaded_path = video_stream.download(output_path="media/videos")

                    filename = os.path.basename(downloaded_path)

                    relative_video_path = f"videos/{filename}"

                    video = VideoFileClip(downloaded_path)

                    audio = video.audio

                    audio_path = "downloads/audio1.wav"

                    audio.write_audiofile(audio_path)

                    audio.close()
                    video.close()

                    transcription = model.transcribe(audio_path)

                    transcript = Transcript.objects.create(
                        title=yt.title,
                        transcript=transcription["text"],
                        segments=transcription["segments"],
                        video_path=relative_video_path,
                        youtube_url=youtube_url
                    )

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

                    transcription = model.transcribe(audio_path)

                    transcript = Transcript.objects.create(
                        title=video_file.name,
                        transcript=transcription["text"],
                        segments=transcription["segments"],
                        video_path=relative_video_path
                    )

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

                    transcription = model.transcribe(audio_path)

                    transcript = Transcript.objects.create(
                        title=audio_file.name,
                        transcript=transcription["text"],
                        segments=transcription["segments"],
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