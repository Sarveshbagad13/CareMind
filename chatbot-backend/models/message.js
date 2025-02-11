const mongoose = require('mongoose');

const messageSchema = new mongoose.Schema({
  userMessage: { type: String, required: true },
  botResponse: { type: String, required: true },
  timestamp: { type: Date, default: Date.now }
});
const Message = mongoose.models.Message || mongoose.model('message', messageSchema);


module.exports = Message;
