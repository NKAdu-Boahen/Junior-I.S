# Adinkra Symbol Recognition

Overview

This project is a web application that recognizes Adinkra symbols using a Convolutional Neural Network (CNN). Users can upload an image of an Adinkra symbol, and the system will classify it and display its meaning.

Features

Deep Learning Model: Trained using TensorFlow/Keras to recognize different Adinkra symbols.

Flask Backend: Serves the model and handles image classification.

React Frontend: Provides a user-friendly interface for uploading and classifying images.

Project Structure
📂 Junior-I.S/
 ├── 📂 backend/            
 │   ├── adinkra_backend.py 
 │   ├── adinkra_model.h5  
 │   ├── class_labels.json  
 │   ├── uploads/           
 │
 ├── 📂 frontend/          
 │   ├── src/
 │   │   ├── AdinkraUploader.jsx 
 │   │   ├── App.js          
 │   │   ├── index.js       
 │
 ├── 📂 dataset/           
 │   ├── train/            
 │   ├── val/               
 │   ├── test/              
 │
 ├── .gitattributes         
 ├── README.md             
 ├── requirements.txt       
