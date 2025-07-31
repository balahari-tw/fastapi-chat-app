# 🧠 GenAI Chat App Backend Using FastAPI

A lightweight backend service for managing chat sessions and messages in a GenAI-powered chat application. This app is built using **FastAPI** and uses in-memory storage (no database) for simplicity and testing purposes.

---

## 🚀 Features

- ✅ Create chat sessions  
- 💬 Add messages to a session  
- 📄 Retrieve chat history (filter by user/assistant role)  
- 🧪 Unit tests with Pytest  
- 🌐 Interactive API documentation via Swagger UI

---

## 🛠️ Technologies Used

- Python 3.9+
- FastAPI
- Uvicorn (server)
- Pytest

---

## 📦 Project Structure
```
fastapi-chat-app/
│
├── app/
│   ├── __init__.py        # Makes 'app' a Python package
│   └── main.py            # FastAPI app with all endpoints
│
├── test/
│   ├── __init__.py        # Optional: Allows test discovery
│   └── test_main.py       # Pytest unit tests for FastAPI endpoints
│
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .venv/                 # Virtual environment
```

---

## ▶️ Getting Started

### 1. Clone the github repository
```bash
git clone https://github.com/bhari-gilead/fastapi-chat-app.git
cd fastapi-chat-app
```

### 2. Set up virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server
```bash
uvicorn app.main:app --reload
```

---

## 📄 Swagger UI - API Documentation
Visit: http://127.0.0.1:8000/docs

---

## 🧪 Running Tests
```bash
pytest tests/test_main.py
```

---

## 📚 API Endpoints

### ✅ 1. Create New Session

#### POST /sessions

**_Request Body:_**
```bash
{
  "session_user": "Bala Hari"
}
```

**_Response:_**
```bash
{
  "session_id": 2,
  "session_user": "bala hari",
  "created_at": "2025-06-30T16:05:00+05:30"
}
```

### 💬 Add Message to Session

#### POST /sessions/{session_id}/messages

**_Request Body:_**
```bash
{
  "role": "user",
  "content": "What is Gen AI?"
}
```

**_Response:_**
```bash
{
  "status": "Message added successfully"
}
```

### 📄 Get Messages from Session

#### GET /sessions/{session_id}/messages

**_Request:_**
* Pass session_id as path
* Pass role as query (optional for filtering messages)

**_Response:_**
```bash
[
  {
    "role": "user",
    "content": "What is Gen AI?"
  },
  {
    "role": "user",
    "content": "What is Agentic AI?"
  }
]
```

---

### 📝 Notes
* The backend uses in-memory lists and dictionaries — all data is lost on server restart.
* created_at timestamp is generated in UTC timezone.
* This project is ideal for prototyping GenAI chat interfaces (or) building a backend POC.
