const { SlashCommandBuilder } = require('discord.js');
const axios = require('axios');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('answer_all')
        .setDescription('Sends all assignments to AI for answering.'),
    async execute(interaction) {
        await interaction.reply({ content: 'Sending all assignments to AI for answering...', ephemeral: true });
        const payload = {
            type: 2,
            data: {
                name: 'answer_all',
                user_id: interaction.user.id,
                channel_id: interaction.channelId
            }
        };
        await axios.post('WEBHOOK_URL', payload);
    },
};
