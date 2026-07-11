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


def format_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02}:{seconds:02}"


def chat(request, transcript_id):

    transcript = get_object_or_404(
        Transcript,
        id=transcript_id
    )

    answer = None
    question = None
    timestamps = []

    if request.method == "POST":

        question = request.POST.get("question")

        if question:

            docs = rag(
                question=question,
                transcript_id=transcript_id
            )
            print("=" * 60)
            print("Retrieved Documents")

            for doc in docs:
                print(doc.metadata)

            if not docs:
                answer = "I couldn't find that information in this video's transcript."

            else:

                context = ""

                for doc in docs:

                    start = doc.metadata.get("start", 0)
                    end = doc.metadata.get("end", 0)

                    timestamps.append({
                        "start": format_time(start),
                        "end": format_time(end),
                        "start_seconds": start,
                        "end_seconds": end
                    })

                    context += (
                        f"[{format_time(start)} - {format_time(end)}]\n"
                        f"{doc.page_content}\n\n"
                    )

                prompt = f"""
You are an AI Video Assistant.

Use ONLY the context provided below to answer the user's question.

Rules:
- Answer only from the provided context.
- Do not invent or assume information.
- If the context is insufficient, reply exactly:
"I couldn't find that information in this video's transcript."
- Keep answers concise unless the user asks for a detailed explanation.

Context:
{context}

Question:
{question}

Answer:
"""

                try:
                    response = model.generate_content(prompt)
                    answer = response.text

                except Exception as e:
                    answer = f"Gemini Error: {str(e)}"

    return render(
        request,
        "rag/chat.html",
        {
            "transcript": transcript,
            "question": question,
            "answer": answer,
            "timestamps": timestamps,
            "video_path": transcript.video_path,
            "youtube_url": transcript.youtube_url,
        }
    )