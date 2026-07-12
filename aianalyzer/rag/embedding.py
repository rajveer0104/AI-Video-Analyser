from inp.models import Transcript
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = None


def get_embedding_model():
    global embedding_model

    if embedding_model is None:
        embedding_model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5",
            encode_kwargs={"normalize_embeddings": True}
        )

    return embedding_model


def create_embeddings(transcript_id):

    transcript = Transcript.objects.get(id=transcript_id)

    segments = transcript.segments

    chunks = []
    metadatas = []

    current_text = ""
    current_start = None
    current_end = None

    chunk_size = 1000

    for segment in segments:

        if current_start is None:
            current_start = segment["start"]

        current_text += segment["text"] + " "

        current_end = segment["end"]

        if len(current_text) >= chunk_size:

            chunks.append(current_text.strip())

            metadatas.append({
                "video_id": transcript.id,
                "title": transcript.title,
                "chunk": len(chunks),
                "start": current_start,
                "end": current_end
            })

            current_text = ""
            current_start = None
            current_end = None

    if current_text:

        chunks.append(current_text.strip())

        metadatas.append({
            "video_id": transcript.id,
            "title": transcript.title,
            "chunk": len(chunks),
            "start": current_start,
            "end": current_end
        })

    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=get_embedding_model(),
        metadatas=metadatas,
        collection_name=f"video_{transcript.id}",
        persist_directory="chroma_db"
    )

    return vectorstore


def rag(question, transcript_id):

    vectorstore = Chroma(
        collection_name=f"video_{transcript_id}",
        persist_directory="chroma_db",
        embedding_function=get_embedding_model()
    )

    docs = vectorstore.similarity_search(
        question,
        k=4
    )

    return docs