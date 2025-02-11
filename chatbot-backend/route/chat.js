/*const express = require('express');
const router = express.Router();
const Message = require('../models/message');

// Endpoint to handle user message
router.post('/message', async (req, res) => {
  const userMessage = req.body.message;

  // Simulate bot response (this can be replaced with actual NLP integration later)
  const botResponse = `You said: ${userMessage}`;

  // Save user message and bot response to MongoDB
  const newMessage = new Message({
    userMessage,
    botResponse
  });

  try {
    await newMessage.save();
    res.json({ response: botResponse });
  } catch (err) {
    res.status(500).json({ error: 'Failed to save message to database' });
  }
});

module.exports = router;*/

