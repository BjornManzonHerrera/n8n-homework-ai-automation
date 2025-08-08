@echo off
cls
echo.
echo [INFO] Activating virtual environment...
call .\venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment.
    exit /b 1
)

echo.

echo [INFO] Installing dependencies from requirements.txt...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies.
    exit /b 1
)

echo.

echo [INFO] Rotating API key...
python rotate_keys.py

echo.

echo [INFO] Loading environment variables...
for /f "tokens=*" %%a in ('python load_env.py') do (call %%a)

echo.

echo [INFO] Starting background services...
start "n8n" n8n start --tunnel
start "Discord Bot" node discord-bot/bot.js

echo.

echo [INFO] Starting ngrok tunnel...
start "ngrok" ngrok http 5678
timeout /t 15
python get_ngrok_url.py > ngrok_url.txt

set /p NGROK_URL=<ngrok_url.txt
if not exist ngrok_url.txt (
    echo [ERROR] ngrok failed to start. ngrok_url.txt not found.
    exit /b 1
)
if not defined NGROK_URL (
    echo [ERROR] ngrok failed. ngrok_url.txt is empty.
    exit /b 1
)
echo [SUCCESS] ngrok tunnel started at: %NGROK_URL%

echo.

echo [INFO] Waiting for n8n to initialize...
timeout /t 15

echo.

echo [INFO] Updating n8n webhook...
curl -X PUT -H "Content-Type: application/json" -H "X-N8N-API-KEY: %N8N_API_KEY%" -d "{\"webhook_url\": \"%NGROK_URL%/webhook/discord-webhook\"}" http://localhost:5678/api/v1/workflows/1


echo.

echo [SUCCESS] Startup sequence complete.
echo.