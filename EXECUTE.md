# Execution Instructions
## Purpose
Define agent-specific tasks and commands for Gemini CLI to execute, debug, or extend the project.

## Agent Roles
- **Coding Agent**:
  - **Tasks**:
    - Generate FastAPI endpoints (`/generate_essay`, `/process_quiz`, `/generate_image`)
    - Implement Discord slash commands (`/get_assignments`, `/approve`)
    - Create OCR script for Canvas PDFs (`ocr_script.py`)
    - Build quiz generator with PDF/Docs output (`quiz_generator.py`)
    - Generate PowerPoint slides (`ppt_generator.py`)
    - Create research paper generator with APA/MLA citations (`paper_generator.py`)
  - **Commands**:
    - `gemini --file api/app.py "Add /generate_essay endpoint using gpt2"`
    - `gemini --file bot/commands/get_assignments.js "Implement /get_assignments command"`
    - Prompt user: `input("Confirm changes to <file>? [y/n]")`
- **Analysis Agent**:
  - **Tasks**:
    - Debug n8n/Make.com workflows (e.g., filter node for essays)
    - Evaluate OCR tools (Tesseract vs. Hugging Face TrOCR)
    - Optimize prompt tuning for essay/quiz/image generation
    - Analyze logs for performance bottlenecks
  - **Commands**:
    - `gemini "Analyze workflows/n8n_workflow.json for filter node errors"`
    - `gemini "Compare Tesseract vs. TrOCR on examples/sample.pdf"`
    - `gemini "Optimize prompt in api/prompts.py for essay quality"`
- **Integration Agent**:
  - **Tasks**:
    - Update n8n/Make.com webhook URLs dynamically
    - Cache Canvas API responses (`cache.json`)
    - Manage Git: Commit changes, push to remote (prompt for repo URL)
    - Add retry logic and Discord error alerts
  - **Commands**:
    - `gemini --file integrate.py "Update webhook URLs and commit to Git"`
    - `curl -X PUT -H "Content-Type: application/json" -d "{\"webhook_url\": \"<ngrok_url>/webhook/discord-webhook\"}" http://localhost:5678/rest/workflows/1`
    - `git add . && git commit -m "<task> integration" && git push origin main`

## General Execution
- **Startup**:
  - Run: `start.bat` to launch n8n, Discord bot, ngrok, and update webhooks
  - Schedule: Use Windows Task Scheduler for daily runs
- **Testing**:
  - Test Discord → Make.com/n8n → FastAPI → Google Docs/Drive
  - Command: `gemini --file test_workflow.py "Generate end-to-end test script"`
- **Version Control**:
  - Prompt for repo URL on first run
  - Confirm commits: `input("Confirm commit? [y/n]")`