# AccessiLearn 🧠🔊

AccessiLearn is a browser-based app designed to help students and educators by providing instant text summarization and read-aloud features.

## Features

- 🧠 AI Summarization using Hugging Face Transformers
- 🔊 Read aloud with speech synthesis
- ⏹️ Toggle to start/stop narration
- 📒 Draggable sticky notes with autosave
- ✨ Typing animation ("AccessiLearn_")
- 🔧 Accessibility toggles:
  - Contrast mode
  - Night mode
  - Large font
  - Dyslexia font

## Tech Stack

- HTML, CSS, JavaScript
- Flask (Python)
- Hugging Face (Transformers)
- Web Speech API
- LocalStorage

## Requirements

```
flask
flask-cors
transformers
torch
sentencepiece
gunicorn
```

## Repo Structure

```
Project/
├── app.py
├── index.html
├── style.css
├── script.js
├── requirements.txt
```

## Deploying on Render

- Upload the full project to GitHub
- Use `gunicorn app:app` as your start command
- Make sure `requirements.txt` is lowercase
- Set Python runtime (3.10+ recommended)
- Update `script.js` API calls to use your Render URL
