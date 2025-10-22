# SHERIA_AI Backend

# ⚖️ LawBot Backend – RAG-Powered Legal Assistant

This is the backend for **LawBot**, a Retrieval-Augmented Generation (RAG) system designed to help users understand **Kenyan labor laws** through a familiar interface — **WhatsApp**.  
The system retrieves relevant legal information and generates natural, conversational answers that can be easily accessed by both employees and employers.

---

## 🚀 Overview

LawBot aims to make legal information, particularly **employment and labor rights**, more accessible to everyday users.  
Users interact with the system via **WhatsApp**, where they can ask questions such as:

> “What are my rights as an employee during termination?”  
> “Can my employer reduce my salary without notice?”

The backend handles:

- Law data ingestion and processing (PDFs, legal documents, etc.)
- Text embedding and vector storage
- Query retrieval using semantic search
- Response generation using a language model
- WhatsApp API communication (via Twilio or similar)

---

## 🧠 RAG (Retrieval-Augmented Generation) Pipeline

Below is the high-level RAG architecture (you’ll fill in details later):

```text
+--------------------+
|  Legal Data Source |
| (PDFs, Text, JSON) |
+---------+----------+
          |
          v
+--------------------+
|  Document Loader   |
| (e.g. PyPDFLoader) |
+---------+----------+
          |
          v
+--------------------+
| Text Splitter      |
| (Recursive Split)  |
+---------+----------+
          |
          v
+--------------------+
| Embedding Model    |
| (e.g. Ollama, OpenAI) |
+---------+----------+
          |
          v
+--------------------+
| Vector Database    |
| (e.g. FAISS)       |
+---------+----------+
          |
          v
+--------------------+
| Retriever          |
| (Top K Chunks)     |
+---------+----------+
          |
          v
+--------------------+
| LLM (Generator)    |
| Generates Answers  |
+---------+----------+
          |
          v
+--------------------+
| WhatsApp Interface |
| (Twilio / Meta API)|
+--------------------+
```
