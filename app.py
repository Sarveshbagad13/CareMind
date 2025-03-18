import json
import random
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Load NLP resources
lemmatizer = WordNetLemmatizer()
with open("intents.json", "r") as file:
    intents = json.load(file)

# Load trained model and data
model = load_model("chatbot_model.h5")
words = pickle.load(open("texts.pkl", "rb"))
classes = pickle.load(open("labels.pkl", "rb"))

# Preprocess user input
def clean_text(sentence):
    tokens = nltk.word_tokenize(sentence)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    return tokens

# Convert text to bag-of-words representation
def bag_of_words(sentence):
    tokens = clean_text(sentence)
    bow = [0] * len(words)
    for token in tokens:
        if token in words:
            bow[words.index(token)] = 1
    return np.array(bow)

# Predict response intent
def predict_intent(user_input):
    bow = bag_of_words(user_input)
    predictions = model.predict(np.array([bow]))[0]
    max_prob_index = np.argmax(predictions)
    
    if predictions[max_prob_index] > 0.7:  # Confidence threshold
        return classes[max_prob_index]
    else:
        return "unknown"

# Generate chatbot response
def chatbot_response(user_input):
    intent = predict_intent(user_input)
    
    for i in intents["intents"]:
        if i["tag"] == intent:
            return random.choice(i["responses"])
    
    return "I'm sorry, I didn't understand that."

# Flask Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_response():
    user_text = request.args.get("msg")
    bot_reply = chatbot_response(user_text)
    return bot_reply

if __name__ == "__main__":
    app.run(debug=True)
