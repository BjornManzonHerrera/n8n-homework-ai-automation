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
:: Prompt for Git repository URL
set /p REPO_URL=Enter remote Git repository URL (e.g., https://github.com/user/repo.git): 
if not exist .git (
    git init
    git remote add origin %REPO_URL%
)
:: Start services
start n8n start --tunnel
timeout /t 15
start node bot/index.js
ngrok http 5678 > ngrok_url.txt
set /p NGROK_URL=<ngrok_url.txt
:: Update n8n webhook
curl -X PUT -H "Content-Type: application/json" -d "{\"webhook_url\": \"%NGROK_URL%/webhook/discord-webhook\"}" http://localhost:5678/api/v1/workflows/1
:: Confirm Git commit
echo Confirm committing changes to Git? [y/n]
set /p CONFIRM= 
if %CONFIRM%==y (
    git add .
    git commit -m "Automated startup, webhook update, and API key rotation"
    git push origin master
)
:: Deactivate virtual environment
deactivate
