# 🧠 Code Analyzer (LLM-Powered)

Analyze source code repositories using state-of-the-art LLMs like **Groq** or **Hugging Face** via LangChain. Returns structured insights as JSON — including summaries, method/function info, and complexity analysis.

Supports:
- 🧠 Multilingual: Python, Java, JS, C++, Go, Rust, etc.
- 🌐 API via FastAPI
- 🖥️ CLI mode
- 🔍 Token-aware chunking
- ✅ Assignment-ready structured output

---

## 📦 Project Structure

code_analyzer/
├── app/
│ ├── api/ # FastAPI routes
│ ├── core/ # logger.py, config
│ ├── services/ # analyzer, cloner, extractor, chunker, file_loader
│ └── templates/ # prompt_template.py
├── cli/ # run_analysis.py
├── tests/ # test_analyzer.py etc.
├── .env # Store your API keys here
├── requirements.txt
├── server.py # FastAPI entry point
├── README.md


---

## 🚀 Option 1: Use Groq (RECOMMENDED)

### 🔐 Step 1: Get Groq API Key
1. Visit [https://console.groq.com](https://console.groq.com)
2. Sign up, go to "API Keys", click "Create API Key"
3. Copy your key (starts with `gsk_...`)

---

### 🧪 Step 2: Set Environment Variable

#### Linux/macOS
### bash
export GROQ_API_KEY="gsk_your_actual_key"

---
### Windows CMD
set GROQ_API_KEY="gsk_your_actual_key"
## PowerShell
$env:GROQ_API_KEY = "gsk_your_actual_key"

## ⚙️ Installation
pip install -r requirements.txt

#### ⚙️ Step 4: Run the code
1. **Run via CLI:** 
    python cli/run_analysis.py https://github.com/janjakovacevic/SakilaProject
2. **Run API with FastAPI:**
   1. uvicorn server:app --reload
   2. Visit Swagger UI: http://localhost:8000/docs
   3. Use the /analyze endpoint with a GitHub repo URL


-----
#### ✅ Assignment Compliance
| Requirement                    | Status |
|-------------------------------|--------|
| 📁 Codebase: SakilaProject     | ✅     |
| ⚙️ Efficient Processing        | ✅     |
| 🤖 LangChain LLM Integration   | ✅     |
| 📏 Token-Aware Chunking        | ✅     |
| 📊 Structured JSON Output      | ✅     |
| ♻️ Modular Code Structure      | ✅     |
| 🌍 Multi-language Support      | ✅     |

-----


#### 🤗 Alternative: Hugging Face Support
🔐 Step 1: Get HF Token
1. Create free account at huggingface.co
2. Go to Access Tokens
3. Create a new token with read access
4. Copy the token (starts with hf_...)

#### 🧪 Step 2: Set the Environment Variable
## Linux/macOS
export HF_TOKEN="hf_your_actual_token_here"
## Windows Command Prompt
set HF_TOKEN="hf_your_actual_token_here"
## Windows PowerShell
$env:HF_TOKEN = "hf_your_actual_token_here"

-----

#### 🛠 Developer Notes
Logging
Logging is handled by app/core/logger.py

Logs appear in the console for both CLI and API

Supported Languages
Python, Java, JavaScript, TypeScript, Go, C/C++, Rust, C#, etc.

Token-Aware Chunking
Code is split into small parts before sending to LLM

Prevents token limit issues in large codebases

----

#### 🔧 Troubleshooting
## "API Key not found"
1. Ensure env var is set correctly
2. Restart terminal
3. Run:
    echo $GROQ_API_KEY   # macOS/Linux
    echo %GROQ_API_KEY%  # Windows CMD

## "Rate limit exceeded"
Groq: 14,400 requests/day (very generous)
Hugging Face: ~1,000/month for free tier
## Model not found
Make sure you're using a supported model name


...

## 📜 License

MIT © 2025 Code Analyzer Authors
