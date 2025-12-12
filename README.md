
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

From: [https://ai.google.dev/](https://ai.google.dev/)

### 2. Add it as an environment variable:

#### Windows (PowerShell)

```bash
setx GEMINI_API_KEY "your-key-here"
```

#### macOS / Linux:

```bash
export GEMINI_API_KEY="your-key-here"
```

**Never** write your key inside any `.py` file.

---

## ▶️ Running the Program

From the project root folder, run:

```bash
python -m src.main
```

This correctly loads the `src` package and allows all imports to work.

---

## 📌 Local Data Storage

The application saves user data in:

```
data/user.txt
data/notes.txt
```

These:

* Are **local only**
* Are **gitignored** (never uploaded)
* Can be deleted anytime to reset the program

---
 🧩 Work in Progress (WIP)

Modules still being expanded:

* Islamic Mode
* Some educational tools
* Some entertainment features
* Additional AI-powered utilities
* Better error handling
* A future Tkinter GUI version



 🎯 Purpose of This Project

This project is designed to develop real Python skills:

* File I/O
* Modular architecture
* Package imports
* API usage
* Environment variables
* Project folder organization
* GitHub readiness

It’s a great foundation for your portfolio and future applications.

---

 Contributing

Feel free to:

* Fork the repo
* Add new modules
* Improve code structure
* Add new calculators or games
* Expand educational content

Pull requests are welcome!

---

 License

This project is free to use for educational and personal purposes.

---
