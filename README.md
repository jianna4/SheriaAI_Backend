# SHERIA_AI Backend

This is the backend for **SHERIA_AI**, a Retrieval-Augmented Generation (RAG) system designed to help users understand **Kenyan labor laws** through a familiar interface — **WhatsApp**.  
The system retrieves relevant legal information and generates natural, conversational answers that can be easily accessed by both employees and employers.

---
## 💡 Problem Statement

Access to legal information in Kenya remains limited due to:
- Complex legal language in acts and regulations  
- Limited public awareness of labor rights  
- Inaccessibility of legal resources to the general public 
There is legal information but certainly a better way to deliver it to users. 

**Sheria_AI** bridges this gap by offering a simple, conversational interface where users can ask questions in plain language and receive accurate, law-based answers.

---

## 🎯 Objectives

1. Develop a **RAG-based backend** capable of retrieving and interpreting Kenyan labor laws.  
2. Provide a **WhatsApp interface** for natural language interaction.  
3. Implement a **vectorized knowledge base** from verified legal sources.  
4. Enable easy **scalability** to other domains such as criminal, land, or family law.

---
## 🚀 Overview

SHERIA_AI aims to make legal information, particularly **employment and labor rights**, more accessible to everyday users.  
Users interact with the system via **WhatsApp**, where they can ask questions such as:

> “What are my rights as an employee during termination?”  
> “Can my employer reduce my salary without notice?”

## Data Sources
The data comes directly from the labour regulations act of kenya.This is a legible source ensuring correct information to the users.

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
