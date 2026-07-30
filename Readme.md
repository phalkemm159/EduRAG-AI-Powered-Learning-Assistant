
# EduRAG – AI-Powered Learning Assistant

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)

An end-to-end **Retrieval-Augmented Generation (RAG)**–based educational assistant that transforms your **video lectures → audio → text → JSON → vector embeddings**, then uses an LLM to answer questions grounded strictly in your own learning material.

EduRAG helps you create your **personal AI teacher** powered by your video content.

---

## 📑 Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [RAG Architecture](#rag-architecture)
- [Features](#features)
- [LLM Integration](#llm-integration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 📘 Introduction
**EduRAG** is an automated pipeline that converts video lectures into an indexed knowledge base that can be queried using any LLM. It uses **Whisper** for speech-to-text, builds vector embeddings, and answers user questions with accurate, content-grounded responses.

---

## 📂 Project Structure
```
EduRAG-AI-Powered-Learning-Assistant/
│
├── audios/                 # Auto-generated audio files (mp3)
├── videos/                 # Place your input video lectures here
├── jsons/                  # Auto-generated JSON transcripts
│
├── whisper/                # Whisper utilities/models (optional)
│
├── video_to_mp3.py         # Converts videos → mp3
├── mp3_to_json.py          # Converts mp3 → JSON using Whisper
├── preprocess_json.py      # Generates embeddings + joblib file
├── process_incoming.py     # Loads embeddings & answers user queries
│
├── prompt.txt              # Prompt template used during RAG inference
├── response.txt            # Optional log of generated answers
└── README.md               # Project documentation
```

---

## 🚀 How It Works

### 1️⃣ Add Your Videos
Place your educational videos inside:
```
/videos
```

### 2️⃣ Convert Videos → MP3
```bash
python video_to_mp3.py
```

### 3️⃣ Convert MP3 → JSON
```bash
python mp3_to_json.py
```

### 4️⃣ Merge JSON + Generate Embeddings
```bash
python preprocess_json.py
```

This creates:
```
final_embeddings.joblib
```

### 5️⃣ Ask Questions Using the RAG System
```bash
python process_incoming.py
```

---

## 🧠 RAG Architecture
```
Videos → Audio → Transcript → JSON → Embeddings → LLM
```

---

## 🔧 Installation

### Install dependencies
```bash
pip install -r requirements.txt
```

### Install Whisper
```bash
pip install openai-whisper
```

---

## ▶️ Usage (Quick Start)
```bash
# 1. Add videos
/videos

# 2. Convert videos → mp3
python video_to_mp3.py

# 3. Convert mp3 → JSON
python mp3_to_json.py

# 4. Create embeddings
python preprocess_json.py

# 5. Ask the AI questions
python process_incoming.py
```

---

## 🤖 LLM Integration
Supports:
- OpenAI GPT models
- Google Gemini Pro
- Llama 3 (local/API)
- Any custom LLM backend

---

## 💡 Features
✔ Automated end-to-end RAG pipeline  
✔ Whisper speech-to-text  
✔ Embeddings stored as joblib  
✔ Accurate, grounded answers  
✔ Semantic retrieval  
✔ Extensible design  

---

## 🛠 Troubleshooting

| Issue | Fix |
|------|------|
| Whisper slow | Use `faster-whisper` or smaller model |
| Missing embeddings | Run `preprocess_json.py` again |
| LLM errors | Check API keys/environment variables |
| Videos not processed | Ensure correct format in `/videos` |

---

## 📬 Contributing
PRs welcome! Add GUIs, more models, optimizations, or retrieval improvements.

---

## 📄 License
MIT License
