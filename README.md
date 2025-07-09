# 📝 Real-Time Collaborative Document Editor

A real-time web application built with **Django**, **Channels**, and **WebSockets** that allows multiple users to edit documents simultaneously with **live AI grammar suggestions** using `TextBlob`.

---

## 🚀 Features

- 🧑‍💻 Real-time collaborative editing using Django Channels
- 🔐 User authentication (signup/login/logout)
- 🧠 Lightweight AI grammar suggestion while typing
- 📃 Document creation and version autosaving
- 👥 Real-time tracking of active editors
- 🌐 WebSocket-based communication for live updates

---

## 📷 Demo Screenshots

> _Add your screenshots here if available_

---

## ⚙️ Tech Stack

- **Backend**: Django 4.x, Django Channels
- **WebSockets**: Channels + Redis
- **Database**: SQLite (default) / PostgreSQL (for production)
- **AI**: TextBlob (offline grammar/spelling correction)
- **Frontend**: Django Templates + JS
- **Deployment**: Daphne + Redis

---

## 📦 Setup Instructions

### ✅ 1. Clone the Repository
git clone https://github.com/yourusername/collabeditor.git
cd collabeditor

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate

3.Install Dependencies
pip install -r requirements.txt

4. Start Redis with Docker
docker run -d --name redis-server -p 6379:6379 redis

5.Run Migrations and Create Superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

6.Run the ASGI Server with Daphne
daphne collabeditor.asgi:application

7. Access the App
Signup: http://127.0.0.1:8000/signup/
Dashboard: http://127.0.0.1:8000/
Create & Edit Docs in Real-Time 🎯
