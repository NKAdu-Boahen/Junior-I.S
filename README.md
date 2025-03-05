# Adinkra Symbol Recognition

Overview

This project is an AI-powered web application that recognizes Adinkra symbols using a Convolutional Neural Network (CNN). Users can upload an image of an Adinkra symbol, and the system will classify it and display its meaning.

Features

Deep Learning Model: Trained using TensorFlow/Keras to recognize different Adinkra symbols.

Flask Backend: Serves the model and handles image classification.

React Frontend: Provides a user-friendly interface for uploading and classifying images.

Git LFS Support: Manages large model files efficiently.

Project Structure
📂 Junior-I.S/
 ├── 📂 backend/            # Flask backend for serving predictions
 │   ├── adinkra_backend.py # Flask API for model inference
 │   ├── adinkra_model.h5   # Trained model (tracked with Git LFS)
 │   ├── class_labels.json  # Mapping of Adinkra symbols
 │   ├── uploads/           # Directory for uploaded images
 │
 ├── 📂 frontend/           # React frontend for user interaction
 │   ├── src/
 │   │   ├── AdinkraUploader.jsx # React component for image upload
 │   │   ├── App.js          # Main React application
 │   │   ├── index.js        # Entry point for React
 │
 ├── 📂 dataset/            # Training dataset
 │   ├── train/             # Training images
 │   ├── val/               # Validation images
 │   ├── test/              # Testing images
 │
 ├── .gitattributes         # Git LFS tracking file
 ├── README.md              # Project documentation
 ├── requirements.txt       # Python dependencies
