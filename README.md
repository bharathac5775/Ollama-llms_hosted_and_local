# 🐳 GenAI Dockerfile Generator

A **GenAI-powered tool** that automatically generates optimized Dockerfiles based on the programming language provided by the user.

This project supports **two execution modes**:

* **Local LLM** using Ollama
* **Hosted LLM** using Google Gemini API

The tool helps developers quickly generate **Dockerfiles that follow container best practices**, including proper base images, dependency installation, working directories, and application execution commands.

---

# 🚀 Features

* Generate Dockerfiles for multiple programming languages
* Support for **local LLM inference (Ollama)**
* Support for **cloud LLM inference (Gemini API)**
* Follows **Docker best practices**
* Simple **command-line interface**
* Easy to extend for more languages or models

---

# 📂 Project Structure

```
ollama/
│
├── local-llms-ollama/
│   ├── generate_dockerfile.py
│   ├── requirements.txt
│   └── .gitignore
│
├── hosted-llm-gemini/
│   ├── generate_dockerfile_gemini.py
│   ├── requirements.txt
│   ├── .env
│   └── .gitignore
│
└── README.md
```

---

# 🖥️ Mode 1 — Local LLM (Ollama)

Generate Dockerfiles using a **local model running with Ollama**.

## Prerequisites

Install Ollama:

### MacOS

```bash
brew install ollama
```

### Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Start Ollama:

```bash
ollama serve
```

Pull a model:

```bash
ollama pull llama3.2:1b
```

---

## Run the Tool

```bash
cd local-llms-ollama
python3 generate_dockerfile.py
```

Example:

```
Enter programming language: python
```

Output:

```
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

---

# ☁️ Mode 2 — Hosted LLM (Gemini API)

Generate Dockerfiles using **Google Gemini cloud models**.

## Prerequisites

Create an API key from **Google AI Studio**.

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## Run the Tool

```bash
cd hosted-llm-gemini
python3 generate_dockerfile_gemini.py
```

Example:

```
Enter the programming language: go
```

Output:

```
FROM golang:1.22-alpine
WORKDIR /app
COPY . .
RUN go mod download
RUN go build -o app
CMD ["./app"]
```

---

# 🔐 Security Notes

* Do **not commit `.env` files** to GitHub.
* Store API keys securely.
* Use `.gitignore` to exclude sensitive files.

Example `.gitignore`:

```
.env
venv
__pycache__
```

---

# 📦 Requirements

For Gemini version:

```
google-genai
python-dotenv
```

For Ollama version:

```
ollama
```

---

# 🛠️ Future Improvements

* Support more programming languages
* Generate **multi-stage Dockerfiles**
* Add **web UI**
* Implement **fallback between local and hosted models**
* Convert tool into a reusable **CLI utility**

---

# 👨‍💻 Author

Developed as a **DevOps + AI learning project** to explore:

* Local LLM inference
* Cloud LLM APIs
* Automated Dockerfile generation

