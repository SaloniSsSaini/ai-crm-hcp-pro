# 🚀 AI-First CRM System for Healthcare Professionals (HCP)
### Intelligent Interaction Logging using LangGraph & LLMs

---

## 📌 Project Overview

This project presents an **AI-first Customer Relationship Management (CRM) system** designed specifically for managing interactions with Healthcare Professionals (HCPs).

Unlike traditional CRMs, this system integrates **agentic AI workflows** using LangGraph and LLMs to enable:

- Conversational interaction logging
- Intelligent data extraction
- Context-aware recommendations
- Memory-driven decision support

The system is built from the perspective of a **life sciences field representative**, ensuring real-world usability and relevance.

---

## 🎯 Core Objective

To design and implement a **Log Interaction Screen** that allows users to:

- Log interactions via structured forms
- Log interactions using natural language chat
- Automatically extract structured insights using AI
- Maintain context using memory of previous interactions

---

## 🧠 Key Features

### 🤖 AI-Powered Interaction Logging
- Natural language input processed using LLM
- Automatic extraction of:
  - HCP Name
  - Interaction Summary
  - Sentiment
  - Follow-up actions

---

### 💬 Conversational AI Interface
- Chat-based interaction logging
- Agent-driven response system using LangGraph
- Context-aware processing with memory integration

---

### 📝 Structured Form Logging
- Manual interaction entry
- Editable AI-generated outputs
- Hybrid UX (AI + Form)

---

### 🧠 Memory-Aware AI
- Retrieves previous interactions
- Enhances decision-making using historical context
- Simulates real-world CRM intelligence

---

### 💡 Smart AI Suggestions
- Recommends next actions
- Suggests follow-ups based on interaction tone
- Enhances sales decision-making

---

### 📊 Analytics Dashboard
- Total interactions
- Sentiment distribution
- Performance insights

---

### 🔊 Voice-Ready Architecture
- Speech-to-Text (input ready)
- Text-to-Speech (output ready)
- Designed for hands-free field usage

---

## 🏗️ System Architecture


Frontend (React + Redux)
↓
Backend (FastAPI)
↓
LangGraph Agent (Decision Engine)
↓
Tool Layer (Modular AI Functions)
↓
Service Layer (Business Logic)
↓
Database (PostgreSQL / SQLite)


---

## 🤖 LangGraph Agent Design

The system uses a **LangGraph-based agent architecture** to orchestrate intelligent workflows.

### 🔹 Agent Responsibilities
- Process user input
- Invoke appropriate tools
- Maintain state and memory
- Generate structured outputs

---

### 🔧 Tools Implemented

| Tool Name | Description |
|----------|------------|
| **Log Interaction Tool** | Extracts structured data using LLM |
| **Edit Interaction Tool** | Allows modification of stored interactions |
| **Suggestion Tool** | Generates AI-driven next steps |
| **Sentiment Tool** | Identifies tone of interaction |
| **Memory Tool** | Retrieves previous interactions |

---

## 🧩 Tech Stack

### 🔹 Frontend
- React.js
- Redux Toolkit
- Axios
- Recharts

### 🔹 Backend
- FastAPI
- SQLAlchemy
- Pydantic

### 🔹 AI & Agent Framework
- LangGraph
- LangChain Core
- Groq LLM (gemma2-9b-it)

### 🔹 Database
- PostgreSQL / SQLite

---

## 🔄 Workflow Explanation

### Step 1: User Input
User enters data via:
- Chat interface OR
- Form input

---

### Step 2: Agent Processing
LangGraph agent:
- Loads memory
- Calls LLM for extraction
- Runs sentiment analysis
- Generates suggestions

---

### Step 3: Data Storage
Processed interaction is stored in the database.

---

### Step 4: Output Delivery
User receives:
- Structured interaction data
- AI insights
- Suggested next steps

---

## 📂 Project Structure


backend/
├── app/
│ ├── api/routes/
│ ├── agents/
│ ├── tools/
│ ├── services/
│ ├── models/
│ ├── schemas/
│ ├── utils/
│ └── core/

frontend/
├── src/
│ ├── components/
│ ├── features/
│ ├── services/
│ └── app/


---

## ⚙️ Setup Instructions

### 🔹 Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
🔹 Frontend Setup
cd frontend
npm install
npm start
🔐 Environment Variables

Create a .env file in the backend directory:

GROQ_API_KEY=your_api_key_here
🧪 API Endpoints
Endpoint	Method	Description
/chat	POST	AI interaction
/interaction	POST	Save interaction
/interaction	GET	Fetch interactions
/analytics	GET	Dashboard data
/voice	POST	Voice input
🎥 Demo Video

👉 Add your video link here

🧠 Key Learnings
Designing AI-first systems using LangGraph
Implementing agent-based workflows
Integrating LLMs into real-world applications
Building scalable backend architecture
Understanding CRM workflows in life sciences
🚀 Future Enhancements
Real-time streaming responses (WebSockets)
Advanced role-based dashboards
Voice-enabled CRM workflows
Predictive analytics for sales
Offline-first mobile support
👩‍💻 Author
Saloni
