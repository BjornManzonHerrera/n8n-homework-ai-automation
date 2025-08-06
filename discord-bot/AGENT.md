Please analyze the current repository, which contains a JavaScript-based Discord bot (using discord.js) for handling slash commands, potentially alongside a FastAPI app and other automation scripts for a Canvas LMS workflow. The bot registers slash commands (e.g., /get_assignments) as defined in files like commands/get_assignments.js. Your task is to ensure these commands integrate with an n8n webhook to trigger a workflow. Follow these steps:

1. **Analyze Existing Command Files**:
   - Identify all command files in the `commands/` directory (e.g., `get_assignments.js`, and four others).
   - Check if each file uses `SlashCommandBuilder` to define a command (e.g., name: "get_assignments", description: "Fetches all assignments from Canvas.") and an `execute` function that sends a placeholder reply (e.g., `interaction.reply('Fetching all assignments from Canvas...')`).
   - Confirm if the files match the requirements in `AGENT.md`, which specify five slash commands with specific names, descriptions, and placeholder replies.

2. **Add Webhook Integration**:
   - For each command file, modify the `execute` function to send an HTTP POST request to an n8n webhook URL (provided as `WEBHOOK_URL`, e.g., `https://abc123.ngrok.io/webhook/discord-webhook`) using the `axios` library.
   - The POST request should include a JSON payload with:
     - `type`: 2 (indicating a Discord slash command interaction).
     - `data`: An object containing:
       - `name`: The command name (e.g., "get_assignments").
       - `user_id`: The ID of the user who triggered the command (`interaction.user.id`).
       - `channel_id`: The ID of the channel where the command was used (`interaction.channelId`).
   - Ensure the `execute` function still sends an ephemeral reply (e.g., `interaction.reply({ content: 'Fetching all assignments from Canvas...', ephemeral: true })`) within 3 seconds, as required by Discord’s API.

3. **Preserve Existing Functionality**:
   - If a command file already matches `AGENT.md` requirements and includes the webhook POST request, leave it unchanged and note this in the output.
   - If a file is missing or incorrect, update it to match the requirements and add the webhook logic.
   - If no command files exist for the required commands, create new ones in the `commands/` directory (e.g., `get_assignments.js`, etc.) with the specified name, description, and webhook integration.

4. **Dependencies**:
   - Ensure the bot includes `axios` for HTTP requests. Add `npm install axios` to installation instructions if needed.
   - Verify `discord.js` is used and included in `package.json`.

5. **Output**:
   - For each of the five command files:
     - State whether it was correct, modified, or newly created.
     - Provide the full code for modified or new files.
   - Include installation instructions (e.g., `npm install discord.js axios`).
   - Note any assumptions or clarifications needed about the repository structure or `AGENT.md` requirements.

6. **Example Code for Reference**:
   Example modified `get_assignments.js`:
   ```javascript
   const { SlashCommandBuilder } = require('discord.js');
   const axios = require('axios');

   module.exports = {
       data: new SlashCommandBuilder()
           .setName('get_assignments')
           .setDescription('Fetches all assignments from Canvas.'),
       async execute(interaction) {
           await interaction.reply({ content: 'Fetching all assignments from Canvas...', ephemeral: true });
           const payload = {
               type: 2,
               data: {
                   name: 'get_assignments',
                   user_id: interaction.user.id,
                   channel_id: interaction.channelId
               }
           };
           await axios.post('WEBHOOK_URL', payload);
       },
   };
   ```

7. **Assumptions**:
   - Assume the n8n webhook URL will be provided as `WEBHOOK_URL` and replaced manually.
   - Assume `AGENT.md` specifies five slash commands with names, descriptions, and placeholder replies, but exact details may vary.
   - If `AGENT.md` or the repository structure is unclear, note this and provide a best-guess implementation based on standard discord.js practices.

Do not modify unrelated files (e.g., FastAPI app) unless necessary for compatibility. Ensure the bot remains functional for registering commands and triggering n8n workflows.