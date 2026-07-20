# 🎥 AI Video Analyzer

An AI-powered Django web application that transforms **YouTube videos, uploaded videos, and audio files** into structured knowledge. Simply paste a YouTube URL or upload your own media, and the application will generate transcripts, create AI-powered summaries, and let you chat with the content using **Retrieval-Augmented Generation (RAG)**.

---

# ✨ Features

- 📺 Analyze YouTube videos using their URL
- 🎥 Upload video files for transcription and analysis
- 🎧 Upload audio files for speech-to-text transcription
- 📜 Fast transcript retrieval for YouTube videos using **Supadata API**
- 🎙️ Automatic speech-to-text transcription for uploaded media using **Faster Whisper**
- 📝 AI-generated structured summaries using **Google Gemini 2.5 Flash**
- 💬 Chat with transcripts using **Retrieval-Augmented Generation (RAG)**
- 🔍 Semantic search powered by **Chroma Vector Database**
- 🧠 Context-aware AI responses using **Gemini**
- ⏱️ Timestamp-aware answers with relevant transcript segments
- ▶️ Jump directly to the relevant timestamp for YouTube videos
- 🔐 User Authentication (Register / Login / Logout)
- 💾 Stores transcripts and summaries for future use

---

# 🛠️ Tech Stack

## Backend

- Django
- Python

## AI & Machine Learning

- Faster Whisper
- Google Gemini 2.5 Flash
- Voyage AI Embeddings
- LangChain
- Chroma Vector Database

## Media Processing

- Supadata API (YouTube Transcript Retrieval)
- MoviePy (Video Audio Extraction)

## Database

- SQLite
- Chroma Vector Database

---

# 📂 Project Structure

```text
AI-Video-Analyzer/
│
├── accounts/          # Authentication
├── inp/               # Input Processing (YouTube, Video & Audio)
├── summary/           # AI Summary Generation
├── rag/               # Retrieval-Augmented Chat
├── analysis/          # Dashboard & Analysis
│
├── downloads/
├── media/
├── chroma_db/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Workflow

```text
                   User Input
            ┌────────┴────────┐
            │                 │
            ▼                 ▼
      YouTube URL      Video / Audio Upload
            │                 │
            ▼                 ▼
     Supadata API      Extract Audio (if video)
            │                 │
            ▼                 ▼
       Transcript      Faster Whisper
            └──────────┬──────────┘
                       ▼
              Store Transcript
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
   Generate Summary         Create Embeddings
     (Gemini 2.5 Flash)        (Voyage AI)
                                   │
                                   ▼
                           Chroma Database
                                   │
                                   ▼
                           User Asks Question
                                   │
                                   ▼
                       Semantic Similarity Search
                                   │
                                   ▼
                     Gemini Generates Grounded Answer
                                   │
                                   ▼
                   Retrieve Relevant Transcript Segments
                                   │
                                   ▼
                      Timestamp-aware Response
```

---

# 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-Video-Analyzer.git
```

### Move into the project directory

```bash
cd AI-Video-Analyzer
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key
SUPADATA_API_KEY=your_supadata_api_key
VOYAGE_API_KEY=your_voyage_api_key
```

---

# ▶️ Running the Project

### Apply migrations

```bash
python manage.py migrate
```

### Create a superuser (Optional)

```bash
python manage.py createsuperuser
```

### Start the development server

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

# 💬 RAG Pipeline

The application uses **Retrieval-Augmented Generation (RAG)** for accurate, context-aware question answering.

1. Retrieve the transcript using **Supadata API** (YouTube) or generate it using **Faster Whisper** (uploaded media).
2. Split the transcript into overlapping chunks.
3. Generate vector embeddings using **Voyage AI**.
4. Store the embeddings in **Chroma Vector Database**.
5. Retrieve the most relevant chunks using semantic similarity search.
6. Pass the retrieved context to **Gemini 2.5 Flash**.
7. Generate an accurate answer grounded in the transcript.
8. Return timestamp-aware responses so users can navigate directly to the relevant section.

---

# 📦 Main Dependencies

- Django
- google-generativeai
- faster-whisper
- voyageai
- langchain
- langchain-chroma
- chromadb
- moviepy
- python-dotenv

---

# 🎯 Supported Input Types

| Input | Supported |
|--------|-----------|
| YouTube URL | ✅ |
| MP4 Video | ✅ |
| MOV Video | ✅ |
| AVI Video | ✅ |
| MP3 Audio | ✅ |
| WAV Audio | ✅ |
| M4A Audio | ✅ |

---

# 🔮 Future Improvements

- 📄 Export summaries as PDF
- 🌍 Multi-language transcription
- 💬 Conversation history
- 👥 Speaker diarization
- 🧠 AI-generated flashcards
- ❓ Automatic quiz generation
- 🗺️ Mind map generation
- 📊 Analytics dashboard
- ☁️ Cloud storage integration

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Rajveer Sanyal

Computer Science Engineering (AI & ML)

If you found this project useful, consider giving it a ⭐ on GitHub!

---
