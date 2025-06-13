# Flask Multiplication Table Generator (with Docker)

This is a simple web application built with Flask that generates the multiplication table for any number entered by the user. The project is fully containerized using Docker, making it easy to build, run, and share.

This project was created as a first step into learning Flask and Docker.

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

---

## 🚀 Features

- **Web-based UI**: Simple and clean interface to enter a number.
- **Dynamic Table Generation**: Displays the multiplication table from 1 to 10.
- **Containerized**: Includes a `Dockerfile` to build a production-ready image.
- **Production Ready**: Uses Gunicorn as the WSGI server for a robust deployment.

---

## 📁 Project Structure

```
/
├── Dockerfile              # Instructions to build the Docker image
├── .dockerignore           # Specifies files to ignore in the Docker build
├── app.py                  # The main Flask application logic
├── requirements.txt        # Python dependencies (Flask, Gunicorn)
└── templates/
    └── index.html          # The HTML template for the user interface
```

---

## 🛠️ Getting Started

Follow these instructions to get the project up and running locally or inside a Docker container.

### 🔧 Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **Docker** and **Docker Desktop**

---

## 💻 Local Development

### Option 1: Running with Python (for Development)

1. **Clone the repository**
   ```bash
   git clone [https://github.com/sarvesh172000/git-learning.git](https://github.com/sarvesh172000/flask-docker-table-app.git)
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask app**
   ```bash
   python app.py
   ```

4. Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🐳 Docker Deployment

### Option 2: Running with Docker (Production)

1. **Build the Docker image**
   > Replace `your-dockerhub-username` with your actual Docker Hub username.

   ```bash
   docker build -t your-dockerhub-username/flask-table-app .
   ```

2. **Run the Docker container**
   ```bash
   docker run -p 8888:8000 your-dockerhub-username/flask-table-app
   ```

3. Open your browser and go to: [http://localhost:8000](http://localhost:8000)

---

## ☁️ Pushing to Docker Hub

To share your image on Docker Hub:

1. **Login to Docker Hub**
   ```bash
   docker login
   ```

2. **Push the image**
   ```bash
   docker push your-dockerhub-username/flask-table-app
   ```

---

## 🧠 Learning Goals

This project is ideal for:

- Beginners learning Flask and web development.
- Exploring how Docker can containerize a Python application.
- Understanding the basics of building and deploying microservices.

---
