const { SlashCommandBuilder } = require('discord.js');
const axios = require('axios');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('get_announcements')
        .setDescription('Retrieves announcements.'),
    async execute(interaction) {
        await interaction.reply({ content: 'Retrieving announcements...', ephemeral: true });
        const payload = {
            type: 2,
            data: {
                name: 'get_announcements',
                user_id: interaction.user.id,
                channel_id: interaction.channelId
            }
        };
        await axios.post('WEBHOOK_URL', payload);
    },
};
