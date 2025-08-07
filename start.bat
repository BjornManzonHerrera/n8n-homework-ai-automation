@echo off
:: Activate virtual environment
call .\venv\Scripts\activate.bat
:: Install dependencies from requirements.txt
if exist requirements.txt (
    echo Installing dependencies from requirements.txt...
    .\venv\Scripts\pip.exe install -r requirements.txt
) else (
    echo requirements.txt not found. Please create it with required dependencies.
    exit /b 1
)
:: Rotate Gemini CLI API key
.\venv\Scripts\pip.exe install python-dotenv
call .\venv\Scripts\python.exe rotate_keys.py
:: Set Git repository URL
git remote set-url origin https://github.com/BjornManzonHerrera/ai-n8n-canvas-discord-bot.git
:: Start services
start n8n start --tunnel
timeout /t 15
start node bot/index.js
ngrok http 5678 > ngrok_url.txt
set /p NGROK_URL=<ngrok_url.txt
:: Update n8n webhook
curl -X PUT -H "Content-Type: application/json" -H "X-N8N-API-KEY: %N8N_API_KEY%" -d "{"webhook_url": "%NGROK_URL%/webhook/discord-webhook"}" http://localhost:5678/api/v1/workflows/1
:: Commit changes
git add .
git commit -m "Automated startup, webhook update, and API key rotation"
git push origin master
:: Deactivate virtual environment
deactivate
