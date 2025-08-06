// deploy-commands.js
const { REST, Routes } = require('discord.js');
require('dotenv').config();

const commands = [
  {
    name: 'get_announcements',
    description: 'Get all announcements from Canvas',
  },
  {
    name: 'get_assignments',
    description: 'Get all assignments from Canvas',
  },
  {
    name: 'get_subject_assignments',
    description: 'Get assignments for a specific subject',
    options: [
      {
        name: 'subject',
        type: 3, // STRING
        description: 'Name of the subject',
        required: true,
      },
    ],
  },
  {
    name: 'get_subject_announcements',
    description: 'Get announcements for a specific subject',
    options: [
      {
        name: 'subject',
        type: 3,
        description: 'Name of the subject',
        required: true,
      },
    ],
  },
  {
    name: 'answer_all_assignments',
    description: 'Trigger answering all assignments via AI',
  },
  {
    name: 'answer_subject_assignments',
    description: 'Answer only assignments from a specific subject',
    options: [
      {
        name: 'subject',
        type: 3,
        description: 'Name of the subject',
        required: true,
      },
    ],
  },
];

const rest = new REST({ version: '10' }).setToken(process.env.BOT_TOKEN);

(async () => {
  try {
    console.log('🚀 Registering slash commands...');

    await rest.put(
      Routes.applicationCommands(process.env.CLIENT_ID),
      { body: commands },
    );

    console.log('✅ Slash commands registered.');
  } catch (err) {
    console.error('❌ Error registering commands:', err);
  }
})();
