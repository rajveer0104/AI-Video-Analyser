# 🎥 AI Video Analyzer

An AI-powered Django web application that transforms **YouTube videos, uploaded videos, and audio files** into structured knowledge. Simply paste a YouTube URL or upload your own media, and the application automatically generates transcripts, creates AI-powered summaries, and lets you chat with your content using **Retrieval-Augmented Generation (RAG)**.

---

# ✨ Features

- 📺 Analyze YouTube videos using their URL
- 🎥 Upload video files for transcription and analysis
- 🎧 Upload audio files for speech-to-text transcription
- 📜 Fast transcript retrieval for YouTube videos using **Supadata API**
- 🎙️ Automatic speech-to-text transcription for uploaded media using **Faster Whisper**
- 📝 AI-generated summaries powered by **Google Gemini 2.5 Flash**
- 💬 Chat with transcripts using **Retrieval-Augmented Generation (RAG)**
- 🔍 Semantic search with **Chroma Vector Database**
- 🧠 Context-aware AI responses using **Google Gemini**
- ⏱️ Timestamp-aware answers with relevant transcript segments
- ▶️ Jump directly to relevant timestamps in YouTube videos
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
├── analysis/          # Analysis Dashboard
├── inp/               # Input Processing (YouTube, Video & Audio)
├── rag/               # Retrieval-Augmented Chat
├── summary/           # AI Summary Generation
│
├── chroma_db/
├── downloads/
├── media/
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
   (Gemini 2.5 Flash)         (Voyage AI)
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
                 Retrieve Relevant Transcript Chunks
                                   │
                                   ▼
                     Timestamp-aware Responses
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

### Install the required dependencies

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

The application uses **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware responses.

1. Retrieve transcripts using **Supadata API** for YouTube videos or generate them with **Faster Whisper** for uploaded video/audio files.
2. Split transcripts into overlapping chunks.
3. Generate embeddings using **Voyage AI**.
4. Store embeddings in **Chroma Vector Database**.
5. Retrieve relevant transcript chunks using semantic similarity search.
6. Pass the retrieved context to **Google Gemini 2.5 Flash**.
7. Generate grounded answers based on the transcript.
8. Return timestamp-aware responses for easy navigation.

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

| Input Type | Supported |
|------------|-----------|
| YouTube URL | ✅ |
| MP4 Video | ✅ |
| MOV Video | ✅ |
| AVI Video | ✅ |
| MKV Video | ✅ |
| MP3 Audio | ✅ |
| WAV Audio | ✅ |
| M4A Audio | ✅ |

---

# 🔮 Future Improvements

- 📄 Export summaries as PDF
- 🌍 Multi-language transcription
- 🧠 Flashcard generation
- ❓ AI-generated quizzes
- 🗺️ Mind map generation
- 📊 Analytics dashboard
- 🏷️ Keyword extraction
- ☁️ Cloud storage integration

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Rajveer Sanyal**

If you found this project helpful, consider giving it a ⭐ on GitHub!
