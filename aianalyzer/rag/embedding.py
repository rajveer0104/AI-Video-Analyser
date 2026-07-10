from inp.models import Transcript

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma


import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini Embedding Model
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    encode_kwargs={"normalize_embeddings": True}
)


def create_embeddings(transcript_id):
    transcript = Transcript.objects.get(id=transcript_id)
    text = transcript.transcript
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=[
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_text(text)

    # Metadata for each chunk
    metadatas = []

    for i in range(len(chunks)):
        metadatas.append({
            "video_id": transcript.id,
            "title": transcript.title,
            "chunk": i + 1
        })

    # Store in ChromaDB
    vectorstore = Chroma.from_texts(
    texts=chunks,
    embedding=embedding_model,
    metadatas=metadatas,
    collection_name=f"video_{transcript.id}",
    persist_directory="chroma_db"
)

    return vectorstore

def rag(question, transcript_id):

    vectorstore = Chroma(
        collection_name=f"video_{transcript_id}",
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )

    docs = vectorstore.similarity_search(
        question,
        k=4
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context