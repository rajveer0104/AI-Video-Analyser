# 🎥 AI Video Analyzer

An AI-powered Django web application that transforms YouTube videos into structured knowledge. Simply provide a YouTube link, and the application will automatically transcribe the video, generate an AI-powered summary, and allow you to chat with the video's content using Retrieval-Augmented Generation (RAG).

---

# ✨ Features

* 📺 Analyze YouTube videos using their URL
* 🎙️ Automatic speech-to-text transcription with Whisper
* 📝 AI-generated structured summaries using Gemini
* 💬 Ask questions about the video using RAG
* ⏱️ Timestamp-aware answers with relevant video segments
* ▶️ Jump directly to the relevant moment in the YouTube video
* 🔍 Semantic search with Chroma Vector Database
* 🧠 Google Gemini for intelligent responses
* 🔐 User Authentication (Register/Login/Logout)
* 💾 Stores transcripts and summaries for future use

---

# 🛠️ Tech Stack

### Backend

* Django
* Python

### AI & Machine Learning

* OpenAI Whisper
* Google Gemini 2.5 Flash
* Google Text Embedding Model (`BAAI BGE-Small-EN-v1.5 (Sentence Transformers)`)
* LangChain
* Chroma Vector Database

### Video Processing

* pytubefix
* MoviePy

### Database

* SQLite (default)
* Chroma DB (Vector Database)

---

# 📂 Project Structure

```text
aianalyzer/
│
├── accounts/          # Authentication
├── inp/               # Video upload & transcription
├── summary/           # AI Summary Generation
├── rag/               # Retrieval-Augmented Chat
├── analysis/          # Video Analysis Module
│
├── downloads/
├── media/
├── chroma_db/
│
├── manage.py
└── requirements.txt
```

---

# ⚙️ Workflow

```text
YouTube URL
      │
      ▼
Download Video
      │
      ▼
Extract Audio
      │
      ▼
Whisper Transcription
      │
      ▼
Store Transcript
      │
      ├────────► Gemini Summary
      │
      └────────► Create Embeddings
                     │
                     ▼
               Chroma Database
                     │
                     ▼
             User asks Question
                     │
                     ▼
          Similarity Search (RAG)
                     │
                     ▼
         Gemini Generates Answer
                     │
                     ▼
 Retrieve Relevant Timestamp
                     │
                     ▼
Open YouTube at that Timestamp
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Video-Analyzer.git
```

Move into the project directory

```bash
cd AI-Video-Analyzer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key
```

---

# ▶️ Running the Project

Apply migrations

```bash
python manage.py migrate
```

Create a superuser (optional)

```bash
python manage.py createsuperuser
```

Start the development server

```bash
python manage.py runserver
```

Open your browser

```
http://127.0.0.1:8000/
```

---

# 💬 RAG Pipeline

The project uses Retrieval-Augmented Generation (RAG) to answer questions accurately.

1. Transcript is split into chunks.
2. Each chunk is converted into embeddings.
3. Embeddings are stored in Chroma DB.
4. User asks a question.
5. Relevant chunks are retrieved using semantic similarity search.
6. Gemini generates an answer grounded in the retrieved transcript context.
7. The system identifies the most relevant timestamp from the retrieved transcript segments.
8. Users can jump directly to the corresponding moment in the YouTube video.

---

# 📦 Main Dependencies

* Django
* google-generativeai
* langchain
* langchain-google-genai
* langchain-chroma
* chromadb
* openai-whisper
* pytubefix
* moviepy
* python-dotenv

---

# 🔮 Future Improvements

* PDF export of summaries
* Multi-language transcription
* Conversation history
* Speaker identification
* Keyword extraction
* Quiz generation from videos
* Analytics dashboard

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Rajveer Sanyal**

If you found this project helpful, consider giving it a ⭐ on GitHub!

