import nltk
import json
import pickle
import random
import numpy as np
import os
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

# 🔹 Ensure necessary NLTK downloads
nltk.download('punkt')
nltk.download('wordnet')

# 🔹 Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# 🔹 Load intents.json file
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

words = []
classes = []
documents = []
ignore_words = ["?", "!", ".", ","]

# 🔹 Tokenization and Lemmatization
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

# 🔹 Lemmatize and clean word list
words = sorted(set(lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words))
classes = sorted(set(classes))

# 🔹 Save processed words and classes
pickle.dump(words, open("texts.pkl", "wb"))
pickle.dump(classes, open("labels.pkl", "wb"))

# 🔹 Create training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = [lemmatizer.lemmatize(w.lower()) for w in doc[0]]
    for w in words:
        bag.append(1 if w in pattern_words else 0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

# 🔹 Shuffle and convert to NumPy array
random.shuffle(training)
train_x = np.array([i[0] for i in training])
train_y = np.array([i[1] for i in training])

# 🔹 Build the Neural Network Model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))

# 🔹 Compile Model
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

# 🔹 Train and Save Model
model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)
model.save("chatbot_model.h5")
print("✅ Model Training Complete!")
