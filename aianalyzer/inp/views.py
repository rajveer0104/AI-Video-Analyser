from django.shortcuts import render,redirect
from .forms import MediaUploadForm
from pytubefix import YouTube
from moviepy import VideoFileClip
from .models import Transcript
import whisper
from rag.embedding import create_embeddings
from django.contrib.auth.decorators import login_required
import os

os.makedirs("downloads", exist_ok=True)


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

            
            if youtube_url:

                result = f"YouTube link received: {youtube_url}"
                yt = YouTube(youtube_url)
                video_stream = yt.streams.get_highest_resolution()
                video_path = video_stream.download(output_path="downloads")
                video = VideoFileClip(video_path)
                audio = video.audio
                audio_path = "downloads/audio1.wav"
                audio.write_audiofile(audio_path)
                

                transcription = model.transcribe(audio_path)
                result=transcription["text"]
                transcript = Transcript.objects.create(
                    title=yt.title,
                    transcript=result
                )
                create_embeddings(transcript.id)
                try:
                    if os.path.exists(audio_path):
                        os.remove(audio_path)

                    if youtube_url and os.path.exists(video_path):
                        os.remove(video_path)

                except Exception:
                    pass
                return redirect(
                    "analysis:analysis",
                    transcript_id=transcript.id
                )
            elif video_file:
                try:
                    video_path = f"downloads/{video_file.name}"
                    with open(video_path, 'wb+') as destination:
                        for chunk in video_file.chunks():
                            destination.write(chunk)
                    video = VideoFileClip(video_path)
                    audio = video.audio
                    audio_path = "downloads/uploaded_audio.wav"
                    audio.write_audiofile(audio_path)
                    transcription = model.transcribe(audio_path)
                    result = transcription["text"]
                    transcript=Transcript.objects.create(
                        title=video_file.name,
                        transcript=result
                    )
                    create_embeddings(transcript.id)
                    try:
                        if os.path.exists(audio_path):
                            os.remove(audio_path)

                        if os.path.exists(video_path):
                            os.remove(video_path)

                    except Exception:
                        pass
                    return redirect(
                        "analysis:analysis",
                        transcript_id=transcript.id
                    )
                except Exception as e:

                    result = f"Error: {str(e)}"
            elif audio_file:
                try:
                    audio_path = f"downloads/{audio_file.name}"
                    with open(audio_path, 'wb+') as destination:
                        for chunk in audio_file.chunks():
                            destination.write(chunk)
                    transcription = model.transcribe(audio_path)
                    result = transcription["text"]
                    transcript=Transcript.objects.create(
                        title="audio_view",
                        transcript=result
                    )
                    create_embeddings(transcript.id)
                    try:
                        if os.path.exists(audio_path):
                            os.remove(audio_path)

                    except Exception:
                        pass
                    return redirect(
                        "analysis:analysis",
                        transcript_id=transcript.id
                    )
                except Exception as e:
                    result = f"Error: {str(e)}"

    else:
        form = MediaUploadForm()

    context = {
        'form': form,
        'result': result
    }

    return render(
        request,
        'inp/home.html',
        context
    )