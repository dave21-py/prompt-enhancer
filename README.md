<p align="center">
  <!-- Replace this logo URL with your own if you have one -->
  <img width="120px" src="https://raw.githubusercontent.com/github/explore/main/topics/prompt-engineering/prompt-engineering.png" alt="Prompt Enhancer logo" />
  <h2 align="center">Prompt Enhancer</h2>
  <p align="center">Fine‑tune your prompts like a pro!</p>
</p>

<p align="center">
  <!-- Shields.io badges you may actually want -->
  <img alt="Gradio" src="https://img.shields.io/badge/UI-Gradio%20v5-blue?logo=gradio" />
  <img alt="Gemini API" src="https://img.shields.io/badge/LLM-Google Gemini‑Flash-green?logo=google" />
  <img alt="Stars" src="https://img.shields.io/github/stars/YOUR‑USERNAME/prompt-enhancer?style=social" />
</p>

<p align="center">
  <a href="#-demo">View Demo</a> ·
  <a href="https://github.com/YOUR‑USERNAME/prompt-enhancer/issues/new?labels=bug&template=bug_report.md">Report Bug</a> ·
  <a href="https://github.com/YOUR‑USERNAME/prompt-enhancer/issues/new?labels=enhancement&template=feature_request.md">Request Feature</a>
</p>

---

### 🚀 Quick Start

```bash
# 1) Clone
git clone https://github.com/YOUR-USERNAME/prompt-enhancer.git
cd prompt-enhancer

# 2) Virtual env
python3 -m venv venv            # Windows:  py -m venv venv
source venv/bin/activate        # Windows:  venv\Scripts\activate

# 3) Install deps
pip install -r requirements.txt   # (Gradio, google‑generativeai, python‑dotenv)

# 4) API key
cp .env.example .env
# edit .env and add:
#   GOOGLE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

# 5) Run
python app.py
# browse ➜ http://127.0.0.1:7860
