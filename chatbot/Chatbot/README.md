
 🧠 Chatbot Portal (Python)

A modular, multi-feature Python console application combining **AI chat**, **weather**, **math tools**, **notes**, **entertainment**, **education**, and more — all inside one interactive program.

This project demonstrates practical Python skills:
file handling, modular programming, API usage, environment variables, and clean project structure.

---

  Features
  1. Login System

* Create accounts (sign-in)
* Login with stored credentials
* Credentials saved locally inside the `data/` folder
* Passwords are not uploaded to GitHub (folder is gitignored)

---

 📝 2. Notes System

* Add notes
* View saved notes
* Notes stored in `data/notes.txt`
* Each user keeps separate local notes

---

 🤖 3. AI Chat

* Uses **Google Gemini**
* Powered by `google-generativeai`
* Reads API key from environment variable: `GEMINI_API_KEY`
* Allows interactive AI conversation

---

 🌦️ 4. Weather Lookup

* Fetches real-time weather data
* Uses public weather APIs
* Simple and beginner-friendly interface

---

 🧮 5. Math Tools

Includes:

* Standard calculator
* Smart calculator (via **numexpr**)
* Geometry calculations
* Temperature converter
* Tip calculator
* (Future) Currency converter

---

 🎮 6. Entertainment Mode

Fun features such as:

* Number guessing
* Magic 8-ball
* Dice roll
* Rock–Paper–Scissors
* Jokes, stories, fun facts

(Some features still being expanded.)

---

 📚 7. Education Mode

* Dictionary
* Country info
* Astronomy facts
* Simple science tools

---

 🕌 8. Islamic Mode (WIP)

Contains placeholders and early features.
Will be expanded in future updates.

---

 🗂 Project Structure

```
chatbot/
│
├── src/
│   ├── main.py              # Entry point (start the app here)
│   ├── auth.py              # Login / sign-in functions
│   ├── ai.py                # AI Chatbot logic
│   ├── general.py           # General utilities
│   ├── entertainment.py     # Games / fun mode
│   ├── islamic_mode.py      # Islamic mode (work in progress)
│   ├── education.py         # Education mode features
│   ├── weather.py           # Weather API logic
│   ├── mathematics.py       # All math-related tools
│   └── main_menu.py         # Menu display + selection
│
├── data/
│   ├── user.txt             # Local user credentials (gitignored)
│   └── notes.txt            # Local notes data (gitignored)
│
├── .gitignore               # Excludes secrets and local data
├── requirements.txt         # Python dependencies
├── README.md                # You are reading it  
```

---

## 🔧 Installation & Setup

### ✔️ 1. Clone the repository

```bash
git clone <your-repo-url>.git
cd chatbot
```

---

### ✔️ 2. (Optional) Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

---

### ✔️ 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 API Key Setup (REQUIRED FOR AI MODE)

The AI chatbot requires a Gemini API key.

### 1. Get your key

# Chatbot

Lightweight, modular command-line chatbot built in Python.

Overview
-
This project provides a modular chatbot framework with multiple topic modules (education, entertainment, mathematics, weather, Islamic mode, and general conversational handlers). It is intended as a simple, extensible example to run locally and to adapt for experiments or learning projects.

Key Features
-
- Modular handlers in `src/` for topics like `education`, `entertainment`, `mathematics`, `weather`, and `islamic_mode`.
- Authentication and basic user data stored under `data/`.
- Single-entry CLI runner in `src/main.py`.

Requirements
-
- Python 3.8+ (create a virtual environment recommended)
- See `requirements.txt` for Python package dependencies

Quick start
-
1. Create and activate a virtual environment:

  ```powershell
  python -m venv .venv
  .\\.venv\\Scripts\\Activate.ps1
  ```

2. Install dependencies:

  ```powershell
  pip install -r requirements.txt
  ```

3. Run the chatbot:

  ```powershell
  python -m src.main
  ```

Project layout
-
- `src/` — Python package containing the chatbot implementation and handlers
  - `main.py` — Entry point to run the chatbot
  - `main_menu.py` — Menu navigation
  - `ai.py`, `auth.py`, `education.py`, `entertainment.py`, `general.py`, `islamic_mode.py`, `mathematics.py`, `weather.py` — Topic modules
- `data/` — Runtime data files (`notes.txt`, `user.txt`)
- `requirements.txt` — Python dependencies

Usage notes
-
- The project is designed for local, interactive use from the command line.
- Edit or extend modules in `src/` to add new behaviors or integrations.
- `data/` contains simple plaintext files used by handlers; back up before editing if needed.

Contributing
-
Contributions are welcome. Open an issue or send a PR with focused changes. Keep changes small and include tests or manual verification steps when appropriate.
