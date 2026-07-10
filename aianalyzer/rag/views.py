from django.shortcuts import render, get_object_or_404

from inp.models import Transcript
from .embedding import rag

import os
from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def chat(request, transcript_id):

    transcript = get_object_or_404(
        Transcript,
        id=transcript_id
    )

    answer = None
    question = None

    if request.method == "POST":

        question = request.POST.get("question")

        if question:

            context = rag(
                question=question,
                transcript_id=transcript_id
            )

            prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context provided below.
Make it precise unless asked for detail.
If asked for details then you can add some contents but strictly related to the context. 
If the answer is not present in the context, reply with:
'I couldn't find that information in this video's transcript.'

Context:
{context}

Question:
{question}

Answer:
"""

            response = model.generate_content(prompt)

            answer = response.text

    return render(
        request,
        "rag/chat.html",
        {
            "transcript": transcript,
            "question": question,
            "answer": answer,
        }
    )