# Initialization Instructions
## Purpose
Guide Gemini CLI in setting up the project environment, installing dependencies, and configuring services.

## Setup Steps
- **Install Dependencies**:
  - **Python (3.10+)**:
    - `pip install -r requirements.txt`
    - Contents of `requirements.txt`:
      ```
      fastapi==0.103.0
      uvicorn==0.23.2
      requests==2.31.0
      python-dotenv==1.0.0
      pytesseract==0.3.10
      pdf2image==1.16.3
      google-api-python-client==2.93.0
      google-auth-oauthlib==1.0.0
      reportlab==4.0.4
      python-pptx==0.6.21
      huggingface_hub==0.16.4
      ```
  - **Node.js (20+)**:
    - `npm install -g n8n discord.js axios`
  - **ngrok**:
    - Install: `npm install -g ngrok` or download from ngrok.com
    - Configure: `ngrok authtoken <token>`
  - **Tesseract**:
    - Install: `choco install tesseract` (Windows) or equivalent
  - **Gemini CLI**:
    - Install: `npm install -g @google/gemini-cli` or Homebrew
- **Environment Setup**:
  - Create `.env` in project root:
    ```
    CANVAS_API_KEY=<key>
    GOOGLE_OAUTH_CLIENT_ID=<id>
    GOOGLE_OAUTH_CLIENT_SECRET=<secret>
    DISCORD_BOT_TOKEN=<token>
    HUGGINGFACE_API_KEY=<key>
    GEMINI_API_KEY=<key>
    NGROK_AUTH_TOKEN=<token>
    ```
  - Start services:
    - n8n: `n8n start --tunnel`
    - Discord bot: `node bot/index.js`
    - FastAPI: `uvicorn app:app --reload`
    - ngrok: `ngrok http 5678`
- **Git Setup**:
  - Initialize: `git init`
  - Prompt user: `Enter remote Git repository URL (e.g., https://github.com/user/repo.git)`
  - Configure remote: `git remote add origin <url>`
  - Initial commit: `git add . && git commit -m "Initial project setup"`
- **Make.com Setup**:
  - Create Canvas module: HTTP request to `https://canvas.instructure.com/api/v1/courses`
  - Configure webhook: `https://<ngrok-id>.ngrok.io/webhook/discord-webhook`
- **Cache Setup**:
  - Create `cache.json` for Canvas API responses