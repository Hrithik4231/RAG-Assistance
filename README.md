# RAG AI Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about them using Google's Gemini AI.

## Features

- 📄 **PDF Upload** - Upload PDF documents to the system
- 🤖 **AI Chat Interface** - Chat-like interface similar to ChatGPT
- 🔍 **Document Retrieval** - Retrieves relevant content from uploaded PDFs
- 💬 **Context-Aware Responses** - AI generates responses based on document context
- 🎨 **Modern UI** - Clean, professional, and user-friendly interface

## Project Structure

```
RAG-AI-Assistant/
├── backend/                 # FastAPI backend
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── pdf_processor.py
│   │   ├── rag_pipeline.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
├── rag-frontend/           # React frontend
│   ├── src/
│   ├── package.json
│   ├── .gitignore
│   └── vite.config.js
└── README.md
```

## Prerequisites

- Python 3.8+
- Node.js 14+
- Google Gemini API Key (get from https://aistudio.google.com/apikey)
- Hugging Face Access Token (get a free one from https://huggingface.co/settings/tokens)

## Setup Instructions

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create .env file:**
   - Copy `.env.example` to `.env`
   - Add your Google Gemini API key and Hugging Face token:
     ```env
     GOOGLE_API_KEY=your_api_key_here
     HF_TOKEN=your_hf_token_here
     ```

6. **Run the backend:**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd rag-frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```
   The app will be available at `http://localhost:5173`

## Usage

1. Upload a PDF document using the **+** button in the chat area
2. Wait for the upload to complete
3. Ask questions about the document in the input field
4. Press Enter to send your query
5. The AI will retrieve relevant content and provide an answer

## Environment Variables

Create a `.env` file in the backend directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
HF_TOKEN=your_hugging_face_token_here
```

**Note:** Never commit `.env` to version control. Use `.env.example` as a template.

## API Endpoints

- `GET /` - Health check
- `POST /upload` - Upload PDF file
- `GET /chat?query=<query>` - Ask a question about the document

## Technologies Used

- **Backend:** FastAPI, ChromaDB, Hugging Face Inference API, Google Generative AI
- **Frontend:** React, Vite, Axios
- **Embeddings:** BAAI/bge-small-en-v1.5, served via the Hugging Face Inference API (no local model download)
- **Vector Store:** ChromaDB

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first.
