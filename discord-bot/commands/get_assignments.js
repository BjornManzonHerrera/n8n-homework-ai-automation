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
