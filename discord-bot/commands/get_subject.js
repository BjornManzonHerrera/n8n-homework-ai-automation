const { SlashCommandBuilder } = require('discord.js');
const axios = require('axios');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('get_subject')
        .setDescription('Fetches assignments for a specific subject.')
        .addStringOption(option =>
            option.setName('subject')
                .setDescription('The subject to fetch assignments for.')
                .setRequired(true)),
    async execute(interaction) {
        const subject = interaction.options.getString('subject');
        await interaction.reply({ content: `Fetching assignments for subject: ${subject}`, ephemeral: true });
        const payload = {
            type: 2,
            data: {
                name: 'get_subject',
                user_id: interaction.user.id,
                channel_id: interaction.channelId,
                options: { subject }
            }
        };
        await axios.post('WEBHOOK_URL', payload);
    },
};
