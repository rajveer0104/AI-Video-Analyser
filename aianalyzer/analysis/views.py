from django.shortcuts import render, get_object_or_404
from inp.models import Transcript

def analysis(request, transcript_id):
    transcript = get_object_or_404(
        Transcript,
        id=transcript_id
    )

    return render(
        request,
        "analysis/index.html",
        {"transcript": transcript}
    )