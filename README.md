# 🐳 GenAI Dockerfile Generator

A GenAI-powered tool that automatically generates **optimized Dockerfiles** based on the programming language provided by the user.

This project uses **Ollama with the Llama3 model** to generate Dockerfiles that follow containerization best practices such as smaller image sizes, proper layering, and efficient dependency management.

---

# 🚀 Features

- Generate Dockerfiles for multiple programming languages
- Uses **Llama3 model via Ollama**
- Follows **Docker best practices**
- Simple command-line interface
- Runs completely **locally**

---

# 📋 Prerequisites

Before running the project, install the following:

## 1️⃣ Install Ollama

### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### MacOS
```bash
brew install ollama
```

---

## 2️⃣ Start Ollama Service

```bash
ollama serve
```

---

## 3️⃣ Pull the Llama3 Model

```bash
ollama pull llama3.2:1b
```

---

# ⚙️ Project Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/dockerfile-generator.git
cd dockerfile-generator
```

---

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

Linux / MacOS

```bash
source venv/bin/activate
```

Windows

```bash
.\venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python3 generate_dockerfile.py
```

Example:

```
Enter programming language: python
```

The tool will generate an **optimized Dockerfile** based on the selected language.

---

# 💡 How It Works

1. The user enters a programming language (Python, Node.js, Java, etc.)
2. The script sends the prompt to the **Ollama API running locally**
3. The **Llama3 model** generates a Dockerfile
4. The generated Dockerfile is displayed with helpful comments

---

# 🧪 Example Output

```
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
```

---

# 🏆 Troubleshooting

- Ensure **Ollama service is running**
- Verify the **Llama3 model is downloaded**
- Check that **Python dependencies are installed**

---

# 📌 Future Improvements

- Support more programming languages
- Add a **web interface**
- Generate **multi-stage Dockerfiles**
- Integrate with **CI/CD pipelines**

---

# 👨‍💻 Author

Developed as a **GenAI + DevOps learning project**.
