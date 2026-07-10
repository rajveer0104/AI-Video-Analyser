from django.shortcuts import render, get_object_or_404

from inp.models import Transcript

import os
from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def summarize(request, transcript_id):

    transcript = get_object_or_404(
        Transcript,
        id=transcript_id
    )

    # If summary already exists, don't generate it again
    if transcript.summary:
        return render(
            request,
            "summary/index.html",
            {
                "title": transcript.title,
                "summary": transcript.summary
            }
        )

    prompt = f"""
You are an AI assistant that summarizes YouTube videos.

Your task is to generate a structured summary using ONLY the transcript below.

Requirements:
- Do not invent information.
- Keep the summary concise but complete.
- Use simple language.
- Mention all major topics discussed.

Format:

## Overview

## Main Topics

## Important Concepts

## Key Takeaways

Transcript:

{transcript.transcript}
"""

    response = model.generate_content(prompt)

    summary = response.text

    # Save the summary so we don't generate it again
    transcript.summary = summary
    transcript.save()

    return render(
        request,
        "summary/summary.html",
        {
            "transcript": transcript,
            "summary": transcript.summary
        }
    )