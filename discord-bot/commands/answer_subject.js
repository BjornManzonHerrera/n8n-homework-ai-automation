const { SlashCommandBuilder } = require('discord.js');
const axios = require('axios');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('answer_subject')
        .setDescription('Sends assignments for a specific subject to AI for answering.')
        .addStringOption(option =>
            option.setName('subject')
                .setDescription('The subject to send assignments for.')
                .setRequired(true)),
    async execute(interaction) {
        const subject = interaction.options.getString('subject');
        await interaction.reply({ content: `Sending assignments for subject ${subject} to AI for answering...`, ephemeral: true });
        const payload = {
            type: 2,
            data: {
                name: 'answer_subject',
                user_id: interaction.user.id,
                channel_id: interaction.channelId,
                options: { subject }
            }
        };
        await axios.post('WEBHOOK_URL', payload);
    },
};
