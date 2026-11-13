# 🔐 AI Escape Room — The Locked Library

An interactive escape room developed using Python, Streamlit, and Google's Gemini API.

## 1. Project Overview

The Locked Library is an AI-assisted escape room where players explore a mysterious library, interact with objects, solve interconnected puzzles, collect a brass key, and unlock the exit door.

The project includes two versions demonstrating the development of an interactive application from a basic prototype into a more advanced, reliable game.

## 2. Project Objectives

- Develop an interactive escape room using Streamlit.
- Integrate Google Gemini as an AI Game Master.
- Implement clickable objects and puzzle-solving interactions.
- Manage player progress using Streamlit Session State.
- Validate puzzle solutions using Python.
- Improve the user interface, inventory management, and error handling between versions.

## 3. Technologies Used

- **Python:** Application development and puzzle logic.
- **Streamlit:** Interactive web interface.
- **Google Gemini API:** AI-powered Game Master.
- **Google Gen AI SDK:** Gemini integration.
- **python-dotenv:** Environment variable management.
- **HTML, CSS, and SVG:** Interface styling and graphical elements.
- **Git and GitHub:** Version control and project portfolio.

## 4. Version 1 — Interactive Prototype

**Status: Implemented**

Version 1 introduces the core interactive escape room experience with a simple library interface.

### Features

- Basic interactive Streamlit interface.
- Four clickable objects: Bookshelf, Desk Drawer, Grandfather Clock, and Exit Door.
- Python-validated puzzle solutions.
- Brass key collection.
- Basic inventory and progress tracking.
- Gemini AI Game Master.
- Local hints when Gemini is unavailable.
- Conversation memory.
- Restart Game functionality.
- Escape completion screen.

## 5. Version 2 — Cinematic Escape Room

**Status: Implemented and gameplay-tested**

Version 2 improves the initial prototype through enhanced presentation, more structured game logic, and stronger interaction handling.

### Improvements

- Cinematic library scene with SVG graphics.
- Improved visual design and object selection.
- Structured Python-managed game state.
- Explicit inventory requirements.
- Deterministic puzzle validation.
- Improved puzzle progression and action restrictions.
- Gemini AI Mode and Local Mode.
- Automatic fallback when Gemini requests fail.
- Visual progress tracking.
- Improved restart functionality.
- Victory screen.

## 6. Version 1 vs Version 2

| Feature | Version 1 | Version 2 |
|---|---|---|
| Interface | Simple interactive library | Cinematic illustrated library |
| Object interaction | Clickable buttons | Enhanced object interactions |
| Puzzle validation | Basic Python validation | Stronger state-dependent validation |
| Inventory | Simple key tracking | Enforced inventory prerequisites |
| Game Master | Gemini with local hints | Gemini and selectable Local Mode |
| Error handling | Basic fallback | Improved automatic fallback |
| Game progress | Basic progress indicator | Enhanced progress display |
| Restart | Supported | Supported |
| Gameplay testing | Basic manual testing | Seven final gameplay tests passed |

## 7. Escape Room Gameplay

The player must investigate four main objects:

1. **Bookshelf:** Discover the combination using numbered books.
2. **Desk Drawer:** Unlock the drawer and collect the brass key.
3. **Grandfather Clock:** Use the brass key to reveal the exit code.
4. **Exit Door:** Enter the correct code to escape.

The puzzles must be completed in the correct sequence.

## 8. Project Structure

```text
AI-Escape-Room/
├── version1/
│   ├── app.py
│   ├── game_prompt.py
│   ├── requirements.txt
│   └── test_gemini.py
├── version2/
│   └── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

The structure above shows the main project files. Additional supporting files may be included.

## 9. Installation and Setup

### Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Escape-Room.git
cd AI-Escape-Room
```

Replace `YOUR_USERNAME` with the actual GitHub username and use the correct repository name.

### Step 2 — Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3 — Install Dependencies

```bash
python -m pip install -r requirements.txt
```

Required libraries:

- streamlit
- google-genai
- python-dotenv

### Step 4 — Configure Gemini

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=your_available_gemini_model
```

Use a Gemini model available to your API key.

Never upload your actual `.env` file to GitHub.

The applications support local hints or Local Mode when Gemini is unavailable.

## 10. Running the Applications

### Run Version 1

```bash
python -m streamlit run version1/app.py
```

### Run Version 2

```bash
python -m streamlit run version2/app.py
```

Open the local URL displayed by Streamlit, usually `http://localhost:8501`.

Stop the running application using `Ctrl + C` before launching the other version on the same port.

## 11. Testing

Version 2 passed seven final manual gameplay tests, covering normal puzzle progression, puzzle restrictions, inventory requirements, escape completion, and restart behavior.

Version 1 was also launched successfully following its interactive interface update.

Automated test coverage and formal usability evaluation have not yet been completed.

## 12. Known Limitations

- Gemini API requests may experience latency or temporary service failures.
- AI-generated responses may occasionally be inconsistent.
- Local gameplay is more predictable because puzzle validation is handled by Python.
- The application currently runs as a local Streamlit project.
- Formal user testing has not yet been conducted.

## 13. Future Improvements

- Additional rooms and puzzle types.
- Difficulty levels.
- Sound effects and animations.
- Save and resume functionality.
- Automated unit and integration tests.
- Deployment to a hosted Streamlit environment.

## 14. Academic Purpose

This project demonstrates the integration of generative AI with traditional application-controlled game logic.

Version 1 establishes the interactive prototype. Version 2 demonstrates improvements in user experience, puzzle validation, reliability, and fallback handling.

The project also serves as a GitHub portfolio example of Python application development, AI integration, interface design, and iterative software improvement.

## 15. Project Status

**Version 1:** Implemented and launched successfully.

**Version 2:** Implemented and passed seven final manual gameplay tests.

**GitHub submission:** Pending final repository verification and upload.