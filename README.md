# 🔐 AI Escape Room — The Locked Library

An AI-powered interactive escape room developed using Python, Streamlit, and Google's Gemini API.

## Project Overview

The Locked Library is a text-based escape room where players explore a mysterious library, investigate objects, solve interconnected puzzles, collect clues, and attempt to unlock the exit door.

The project is developed in two versions to demonstrate the differences between AI-managed gameplay and structured application-controlled game logic.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI Python SDK
- python-dotenv
- Git and GitHub

## Version 1 — LLM-Controlled Escape Room

**Status: In Development**

Version 1 uses Gemini as an AI Game Master to interpret player commands, generate responses, and manage puzzle progression through conversation history.

### Implemented Features

- Streamlit-based interactive interface
- Gemini API integration
- Game Master system prompt
- Natural-language player commands
- Conversation memory using Streamlit Session State
- Restart Game functionality
- Automatic opening scene
- Initial escape completion detection

### Escape Room Objects

1. Bookshelf
2. Wooden desk
3. Painting
4. Locked drawer
5. Grandfather clock
6. Exit door

### Puzzle Structure

Players must discover a bookshelf combination, unlock a drawer, collect a brass key, investigate a grandfather clock, and obtain the final exit code.

### Current Limitations

- Gemini responses can be slow, sometimes exceeding two minutes.
- Puzzle progression is controlled by the language model rather than independently validated Python state.
- Complete gameplay and adversarial testing are pending.
- Escape completion detection requires further testing.

## Version 2 — Structured Game State

**Status: Planned**

Version 2 will improve reliability by introducing:

- Python-managed game state
- Explicit inventory management
- Deterministic puzzle validation
- Action validation and error handling
- Improved protection against invalid or contradictory player actions
- Comparative testing against Version 1

## Project Structure

```text
AI-Escape-Room/
├── version1/
│   ├── app.py
│   ├── game_prompt.py
│   ├── requirements.txt
│   └── test_gemini.py
├── .env.example
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Escape-Room.git
cd AI-Escape-Room
```

Replace `YOUR_USERNAME` with the repository owner's GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r version1/requirements.txt
```

### 4. Configure Gemini

Create a `.env` file in the project root using `.env.example` as a template.

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=your_available_gemini_model
```

Use a Gemini model available to your API key.

Never commit your actual `.env` file or API key.

### 5. Run the application

```bash
python -m streamlit run version1/app.py
```

Open the local Streamlit URL displayed in the terminal, usually `http://localhost:8501`.

## Development Progress

| Component | Status |
|---|---|
| Project setup | Completed |
| Streamlit interface | Implemented |
| Gemini integration | Implemented |
| Game Master prompt | Implemented |
| Conversation memory | Implemented |
| Restart functionality | Implemented |
| Escape completion detection | Initial implementation |
| Performance optimization | Pending |
| Complete gameplay testing | Pending |
| Version 2 | Planned |
| Final comparison and report | Pending |

## Academic Purpose

This project demonstrates the capabilities and limitations of large language models in interactive applications. Version 1 explores LLM-controlled gameplay, while Version 2 will investigate whether structured Python state and validation improve reliability, consistency, and robustness.

## Development Status

The application is under active development. Features, documentation, tests, and implementation details will be updated through subsequent GitHub commits.