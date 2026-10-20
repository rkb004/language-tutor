
# Telugu Language Tutor

A local AI-powered conversational tutor built with Python, FastAPI, and Ollama to help English-speaking learners practice Telugu through natural dialogue.

The project focuses on Romanized Telugu, allowing users to learn conversational Telugu using English letters without needing to read or write Telugu script.

## Overview

The goal of Telugu Language Tutor is to make language learning more conversational and personalized.

Rather than relying exclusively on vocabulary memorization, the application uses a locally hosted language model to simulate everyday conversations, provide translations, explain grammar, and help users practice constructing sentences.

The backend is designed around three main components:

1. A FastAPI service for handling requests.
2. An Ollama integration for generating conversational responses.
3. A session-based memory system for maintaining conversation context.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Backend Framework | FastAPI |
| Language Model | Llama 3.1 via Ollama |
| Model Communication | REST API |
| Data Validation | Pydantic |
| Conversation Memory | Python in-memory storage |
| Testing | pytest |

## Features

### Conversational Telugu Practice

The application provides a conversational interface through an API, allowing learners to submit messages and receive AI-generated Telugu responses.

The tutor is configured to:

- Respond using Romanized Telugu.
- Provide English translations when helpful.
- Explain grammar and vocabulary.
- Correct mistakes in a conversational manner.
- Ask follow-up questions to encourage continued practice.

### Adaptive Difficulty Levels

The API supports three learning levels:

- Beginner: Basic vocabulary, greetings, and short sentences.
- Intermediate: Longer conversations and sentence construction.
- Advanced: Natural conversations and more complex expressions.

Difficulty levels influence the system prompt sent to the language model.

### Conversation Memory

The application maintains separate conversation histories using session IDs.

Recent messages are included in subsequent model requests, allowing the tutor to maintain context throughout a conversation.

The memory system includes:

- Session-based message storage.
- Chronological conversation history.
- Configurable message limits.
- Session retrieval and clearing.

### Local LLM Integration

Ollama provides the interface for running language models locally.

The tutor constructs a system prompt, combines it with recent conversation history, and sends the request to the Ollama chat API.

The default model is Llama 3.1 8B, although the model can be configured using environment variables.

## Project Structure

```text
language-tutor/
├── app/
│   ├── main.py
│   ├── services/
│   │   ├── tutor.py
│   │   └── memory.py
│   └── __init__.py
├── tests/
│   └── test_tutor.py
├── docs/
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Project information |
| GET | /health | API health check |
| POST | /chat | Generate a tutor response |
| GET | /history/{session_id} | Retrieve conversation history |
| DELETE | /history/{session_id} | Clear conversation history |

## Example Interaction

User: How do I say "I'm going to the store"?

Tutor:

Telugu: Nenu shop ki velthunnanu.

English: I'm going to the store.

Explanation: "Nenu" means "I," and "velthunnanu" describes the action of going somewhere.

Practice: How would you say "I'm going home"?

This is an illustrative example of the intended conversational format.

## Running Locally

### Requirements

- Python 3.10 or newer
- Ollama
- A compatible local language model

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Download the Language Model

```bash
ollama pull llama3.1:8b
```

### 3. Start the Backend

```bash
uvicorn app.main:app --reload
```

### 4. Access the API

Open the interactive API documentation:

http://localhost:8000/docs

### 5. Send a Message

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Teach me how to introduce myself",
    "difficulty": "beginner"
  }'
```

## Testing

The repository includes unit tests for conversation memory and tutor prompt configuration.

Run the tests using:

```bash
pytest
```

These tests do not require an active Ollama model. Live model responses have not been independently verified.

## Engineering Decisions

### Local-First Architecture

The application uses Ollama to communicate with locally hosted language models, avoiding reliance on external inference APIs.

### Romanized Telugu

The tutor prioritizes spoken Telugu using English characters. This makes conversational practice accessible to learners who are not familiar with Telugu script.

### Context-Aware Conversations

Recent conversation history is passed to the model with each request, supporting continuity between interactions.

### Modular Backend

The API, model interaction, and conversation memory are separated into individual modules to keep the code organized and maintainable.

## Project Status

This repository contains a backend source-code prototype.

The code includes FastAPI endpoints, Ollama integration logic, conversation memory, and unit tests. The application has not been deployed or validated end to end.

## Author

Rachit Bandaram

Computer Science — University of Wisconsin–Madison

GitHub: https://github.com/rkb004

