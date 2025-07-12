# 🧠 AccessiLearn: AI-Powered Summarization for Inclusive Learning

AccessiLearn is a browser-based tool designed to make reading and understanding content more accessible for students and educators. It summarizes long text using artificial intelligence and offers voice playback, visual enhancements, and note-taking—all in a clean, distraction-free interface.

## 🚀 Why AccessiLearn?

Modern education isn't always designed with accessibility in mind. Learners who face challenges like cognitive load, vision impairments, or dyslexia need extra tools—not fewer options. AccessiLearn was built during the **Coders Club Hackathon 2025** to solve this gap with simplicity and thoughtful design.

---

## ✨ Core Features

- 🧠 AI Summarization using Hugging Face's BART-Large-CNN model  
- 🔊 Read Aloud Toggle using Web Speech API  
- ⏹️ Start/Stop voice playback with intuitive controls  
- 📒 Sticky Notes saved with LocalStorage  
- 🎩 Typing Animation: “AccessiLearn_”  
- 🌓 Accessibility Modes: High contrast, large font, dyslexia font, and night mode  

---

## 🛠️ Tech Stack

| Layer     | Technology                    |
|-----------|-------------------------------|
| Frontend  | HTML, CSS, JavaScript         |
| Backend   | Flask, Gunicorn               |
| AI Model  | Hugging Face Transformers     |
| Voice     | Web Speech API                |
| Hosting   | GitHub Pages + Render         |
| Storage   | LocalStorage (Notes, Toggles) |

---

## 🧪 How It Works

1. Type or paste any paragraph  
2. Click "Summarize" → sends request to Hugging Face API  
3. Receive a concise summary + optional voice playback  
4. Customize your experience with sticky notes and toggles  

---

## 🐙 Repository Structure

```
AccessiLearn/
├── app.py
├── requirements.txt
├── index.html
├── style.css
├── script.js
├── templates/
│   └── index.html
├── Final Record.mp4
```

---

## 🌍 Live Demo

🔗 [Visit AccessiLearn](https://naik-datta8237.github.io/Project)

🖥️ Hosted via GitHub Pages (frontend) & Render (backend Flask API)

---

## 📦 Installation

Install dependencies locally:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
python app.py
```

---

## 🎥 Demo Video

📺 [Watch Final Record][![Watch the demo](https://img.youtube.com/vi/O9g7gsTRsLE/0.jpg)](https://www.youtube.com/watch?v=O9g7gsTRsLE)


---

## 🤝 Built for Coders Club Hackathon 2025

Designed with creativity, inclusiveness, and storytelling at its heart. AccessiLearn aims to make digital education friendlier for everyone.
