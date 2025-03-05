from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained model
model = tf.keras.models.load_model("adinkra_model.h5")

# Load class labels
with open("class_labels.json", "r") as f:
    class_names = json.load(f)

# Dictionary of meanings
symbol_meanings = {
    'aban': 'Symbol of strength and security',
    'akoma': 'Symbol of patience and endurance',
    'boa me na me boa wo': 'Symbol of cooperation and interdependence',
    'duafe': 'Symbol of cleanliness and love',
    'gye nyame': 'Symbol of the supremacy of God',
    'nsoroma': 'Symbol of hope and guidance',
    'nyame dua': 'Symbol of God’s presence and protection',
    'ohene': 'Symbol of leadership and authority',
    'sankofa': 'Symbol of learning from the past',
    'sunsum': 'Symbol of the spirit and soul'
}

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    img_array = preprocess_image(file_path)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    confidence = float(np.max(predictions[0]))  # Convert float32 to Python float

    if confidence < 0.6:
        return jsonify({"symbol": "Not an Adinkra symbol", "confidence": confidence})

    symbol = class_names.get(str(predicted_class), "Unknown")
    meaning = symbol_meanings.get(symbol, "Meaning not found")
    
    return jsonify({"symbol": symbol, "meaning": meaning, "confidence": confidence})


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
