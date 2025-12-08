# 💡 Meme-Based Emotional Support Chatbot

A **RAG-powered emotional support chatbot** designed for young users, combining **network memes, humor, and empathy** to deliver more natural, engaging, and emotionally resonant AI conversations.

---

## 🔍 Background

As emotional stress and the demand for “emotional value” increase among younger generations, most existing emotional chatbots suffer from:

- Template-like and emotionally shallow responses  
- Poor understanding of internet memes, leading to awkward or misplaced usage  
- A disconnect between humor and meaningful emotional support  

This project addresses these issues by integrating **Retrieval-Augmented Generation (RAG)** with **hybrid retrieval and controllable style prompting**, enabling AI responses that are humorous yet empathetic, structured yet natural.

---

## ✨ Key Features

- ✅ **Emotion–Scene–Meme three-dimensional matching mechanism**
- ✅ **Hybrid retrieval using BM25 + FAISS + RRF fusion**
- ✅ **Two-stage generation pipeline for logical correctness and stylistic fluency**
- ✅ **Multi-style controllable outputs** (sarcastic / gentle / high-meme-density)
- ✅ **End-to-end runnable system** with multi-turn dialogue and user preference modeling

---

## 🧠 System Overview
User Input
↓
Rational Response Generation (LLM)
↓
Hybrid Retrieval (BM25 + FAISS)
↓
RRF Fusion & Re-ranking
↓
Style Prompt Injection
↓
Meme-enhanced Generation
↓
Final Response + Preference Update

---

## ⚙️ Technical Approach

### 1. Hybrid Retrieval & Meme Matching

- Vectorized **400+ internet memes** using  
  **HuggingFaceEmbeddings (BGE-large-zh-v1.5)**
- Built:
  - **FAISS** semantic vector index
  - **BM25** keyword inverted index
- Applied **Reciprocal Rank Fusion (RRF)** to merge dual retrieval results

📈 **Results**
- Meme-matching accuracy improved from **68% to 85%**
- Significantly reduced semantic ambiguity in polysemous and cross-context scenarios

---

### 2. Two-Stage Generation Pipeline

**Stage 1: Rational Response Generation**

- Generates logically sound and structured base responses
- Ensures semantic correctness and actionable suggestions

**Stage 2: Style-Aware Rewriting**

- Injects retrieved memes via a structured prompt template:
Humorous Teasing → Emotional Empathy → Actionable Advice


- Supports dynamic control of:
  - Meme density (k-value)
  - Response style (sarcastic / gentle / expressive)

📈 **Results**
- Response naturalness score improved from **3.2 to 4.3 / 5**
- User preference rate increased by **51%**

---

## 🧪 Data & Training

- Constructed **2,000+ RAG-enhanced training samples**
- Training format:
User Query + Rational Answer + Retrieved Memes + Style Instructions

- Improved model alignment with meme-aware emotional expression and contextual humor

---

## 🛠 Tech Stack

- **Python**
- **LangChain**
- **FAISS**
- **BM25 (rank_bm25)**
- **HuggingFace Embeddings**
- **Baidu Qianfan / Doubao LLMs**
- **Gradio** (interactive UI)

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python run.py
```
Launches a local Gradio interface for interactive testing.

## 📌 Highlights

Not a simple meme generator, but a controlled, explainable, and evaluable emotional support system

Focuses on retrieval design and prompt engineering, rather than heavy model fine-tuning

Balances algorithmic rigor, system design, and user experience metrics
