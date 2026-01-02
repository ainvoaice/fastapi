# AI-Enhanced Data Module

**Candidate:** FS
**Company:** InnoVyne
**Stack:** FastAPI (Backend) · Next.js / React (Frontend) · Haystack (Agency Framework) · OpenAI (LLM Model)

---

## Overview

This repository contains my implementation of the **AI-Enhanced Data Module** exercise for InnoVyne.
The goal of this project is to demonstrate how I design, build, and reason about a small but extensible full‑stack system that combines **data ingestion**, **interactive data exploration**, and **AI‑assisted analysis**.

The solution focuses on **clarity of architecture**, **pragmatic trade‑offs**, and **velocity**, aligning with how small, fast‑moving product teams typically work.

---

## Features

### 1. Data Ingestion

* Upload structured data via:

  * **CSV**
  * **JSON**(pending)
  
* Designed for extensibility to support additional formats:

  * PDF / DOCX (document parsing layer)
  * Image (OCR pipeline)
* Transmission methods (pluggable design):

  * Direct upload (current)
  * Email ingestion (future)
  * FTP ingestion (future)

### 2. Interactive Data Table

* Client‑side table rendering with:

  * Column filtering
  * Sorting
  * Pagination for large datasets
* Inline editing:

  * Edit existing cells
  * Add new rows
* Changes are synced back to the backend via REST APIs

### 3. AI Assistant Panel

* Context‑aware assistant connected to the uploaded dataset
* Supported interactions:

  * **Data summary** (key statistics, trends, anomalies)
  * **Natural language Q&A** (e.g. “Which product had the highest sales?”)
* Designed as a lightweight RAG‑style workflow:

  * Data → structured context → LLM prompt

---

## Architecture

```
Next.js (React)
│
├── Data Upload UI
├── Interactive Table
├── AI Assistant Panel
│
└── API Layer (REST)
        │
        ▼
FastAPI Backend
│
├── File Ingestion & Validation
├── Data Normalization Layer
├── Data Store (in‑memory / DB abstraction)
├── AI Service (LLM integration)
└── Security & Error Handling
```

### Frontend (Next.js)

* React‑based UI optimized for fast iteration
* Clear separation of concerns:

  * Table state management
  * AI interaction state
  * API communication layer
* Designed to scale toward server components and streaming responses

### Backend (FastAPI)

* Chosen for:

  * Strong typing
  * High performance
  * Excellent async support
* Responsibilities:

  * File parsing & validation
  * Data persistence abstraction
  * AI prompt orchestration
  * Clean, well‑documented REST endpoints

---

## AI Design Approach

Instead of a complex agent framework, the AI assistant uses a **focused, deterministic pipeline**:

1. Normalize uploaded data into a structured representation
2. Extract lightweight metadata (columns, types, aggregates)
3. Inject data context into a constrained prompt
4. Return concise, explainable responses

**Rationale:**

* Faster iteration
* Predictable outputs
* Easier to debug and extend

This approach mirrors real‑world product constraints where reliability and explainability often outweigh sophistication.

---

## Trade‑Offs & Design Decisions

* **In‑memory data store (initially)**

  * Faster development
  * Easily replaceable with Postgres / DuckDB

* **REST over WebSockets**

  * Simpler mental model
  * Sufficient for current interaction patterns

* **Minimal AI abstraction**

  * Avoided over‑engineering
  * Focused on product value instead of framework complexity

---

## Running Locally

### Prerequisites

* Node.js 18+
* Python 3.10+

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on `http://localhost:3000`
Backend runs on `http://localhost:8000`

---

## What I’d Improve With More Time

* Persistent storage with versioned datasets
* Background ingestion jobs for large files
* Streaming AI responses for better UX
* Role‑based access control
* Deeper anomaly detection and statistical insights

---

## How This Aligns With InnoVyne

This project reflects how I approach engineering problems:

* Build **end‑to‑end ownership** quickly
* Make **intentional trade‑offs**
* Optimize for **product learning**, not just code

I’m looking forward to discussing the technical details, design choices, and potential next steps during the technical deep dive and project presentation.

---

Thanks for reviewing!
