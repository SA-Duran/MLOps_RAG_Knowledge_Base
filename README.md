# MLOps_RAG_Knowledge_Base
# MLOps RAG Knowledge Base

## Overview  
This project implements a **Retrieval-Augmented Generation (RAG)** pipeline with document upload, vector indexing, and LLM-based conversational QA. Users can upload `.pdf` or `.txt` documents, which are embedded and stored for retrieval. The system responds to natural language queries using OpenAI’s GPT‑3.5 with relevant context pulled from the indexed documents.

---

## 🔧 Architecture & Components

The system is modular and composed of the following services:

### 1. `main.py` — Flask App Interface  
- Exposes REST API endpoints:
  - `/upload`: Accepts `.pdf` or `.txt` files, splits them, indexes them, and uploads to S3.
  - `/query`: Accepts a natural language question, returns a generated answer.
- Integrates all other services.

### 2. `vector_store.py` — Document Embedding & Vector DB  
- Uses **OpenAI embeddings** + **ChromaDB** via LangChain.  
- Stores document chunks and enables similarity search based on user queries:contentReference[oaicite:0]{index=0}.

### 3. `llm_service.py` — Conversational Agent  
- Implements a **ConversationalRetrievalChain** with:
  - OpenAI GPT‑3.5 (`ChatOpenAI`) as the LLM.
  - Vector store retriever.
  - Memory via `ConversationBufferMemory` for multi-turn dialogue:contentReference[oaicite:1]{index=1}.

### 4. `storage_service.py` — AWS S3 Integration  
- Uploads original files to **Amazon S3**.  
- Retrieves files using `boto3` and user-configured bucket/region settings:contentReference[oaicite:2]{index=2}.

### 5. `config.py` — Environment Configuration  
- Loads secrets (OpenAI key, AWS region, bucket name) via `.env` file:contentReference[oaicite:3]{index=3}.

---

## 🔗 Tech Stack

| Category             | Tools / Libraries                     |
|----------------------|----------------------------------------|
| Web Server / API     | Flask                                  |
| Embedding Model      | `OpenAIEmbeddings` (via LangChain)     |
| Vector DB            | ChromaDB (`langchain.vectorstores`)    |
| LLM Engine           | GPT‑3.5 (`langchain.chat_models`)      |
| Document Parsing     | PyPDFLoader, TextLoader                |
| Chunking Strategy    | RecursiveCharacterTextSplitter         |
| File Storage         | AWS S3 via `boto3`                     |
| Configuration        | `python-dotenv` + `Config` class       |
| CI/CD (optional)     | GitHub Actions + `cicd.yaml`           |
| Containerization     | Docker (Dockerfile not uploaded)       |

---

## 📦 Installation

```bash
git clone https://github.com/SA-Duran/MLOps_RAG_Knowledge_Base.git
cd MLOps_RAG_Knowledge_Base
pip install -r requirements.txt
```

You’ll need to define the following in a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
AWS_REGION=your_aws_region
AWS_BUCKET_NAME=your_bucket_name
```

---

## 🚀 Usage

### 📝 Upload a Document

```bash
curl -X POST http://localhost:8080/upload \
  -F 'file=@/path/to/your/file.pdf'
```

This will:
- Parse and chunk the document
- Store the original in S3
- Embed and index it for future queries

### ❓ Ask a Question

```bash
curl -X POST http://localhost:8080/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is this document about?"}'
```

The system will:
- Retrieve relevant chunks from the vector DB
- Pass them along with the question to GPT‑3.5
- Return a synthesized answer

---

## 🧪 Example Query Flow

1. Upload a PDF with regulatory or technical documentation.
2. Ask:  
   ```
   "What are the safety requirements mentioned in this document?"
   ```
3. Get a precise, context-aware answer from the LLM.

---

## 📁 Supported File Types

- `.pdf`
- `.txt`

---

## 📄 License

MIT License (add `LICENSE` file if not yet present)

