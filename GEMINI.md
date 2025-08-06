# Global Gemini CLI Context
## Purpose
Provide default coding standards, security practices, and automation rules for all projects using Gemini CLI.

## Rules
- **Languages**: Python 3.10+, JavaScript (Node.js 20+)
- **Coding Style**:
  - Python: Adhere to PEP 8 (e.g., 4-space indentation, descriptive variable names)
  - JavaScript: Follow Airbnb JavaScript Style Guide (e.g., camelCase, semicolons)
- **Error Handling**:
  - Include try-except blocks for API calls in Python
  - Use try-catch for async JavaScript functions
  - Log errors to console and file (e.g., `errors.log`)
- **Output**:
  - Generate modular, commented code
  - Avoid excessive verbosity in responses
- **Dependencies**:
  - Python: Use `requirements.txt` for dependency management
  - JavaScript: Use `package.json` for Node.js dependencies
- **Security**:
  - Store API keys in `.env` (e.g., Canvas, Google, Discord, Hugging Face, Gemini)
  - Never hardcode sensitive data
- **Version Control**:
  - Use Git for all projects
  - Commit with descriptive messages (e.g., "Added /generate_essay endpoint")
  - Prompt user for confirmation before modifying files or committing
- **Automation**:
  - Prefer scripts for repetitive tasks (e.g., startup, webhook updates)
  - Include user confirmation for file changes (e.g., `input("Confirm changes? [y/n]")`)