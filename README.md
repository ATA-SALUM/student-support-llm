# University Student Support Assistant (Self-Hosted LLM)

## Project Overview

This project implements a full-stack AI application using a locally hosted Large Language Model (LLM). The application assists university students by answering questions related to university services such as course registration, examination rules, library services, ICT support, hostel applications, fee payment, academic calendar, and student conduct.

The project demonstrates the complete deployment pipeline of an LLM application, including backend API development, frontend interface, logging, testing, and documentation.

## Technologies Used

* Python 3.14
* FastAPI
* Streamlit
* Ollama
* Llama3.2:1b
* Uvicorn
* Requests
* Logging Module

## Project Structure

```text
student-support-llm/
├── backend/
├── frontend/
├── tests/
├── docs/
├── requirements.txt
└── README.md
```

## Installation

1. Create virtual environment

```bash
python -m venv venv
```

2. Activate

```bash
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run Ollama

```bash
ollama run llama3.2:1b
```

5. Start backend

```bash
cd backend
uvicorn main:app --reload
```

6. Run frontend

```bash
cd frontend
streamlit run app.py
```

## Features

* Local LLM
* FastAPI Backend
* Streamlit Frontend
* Logging
* Error Handling
* API Testing

## Testing

Swagger UI

```
http://127.0.0.1:8000/docs
```

Health Endpoint

```
http://127.0.0.1:8000/health
```

## Authors

IS365 Practical Assignment
