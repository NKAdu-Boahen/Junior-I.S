import { useState } from "react";

export default function AdinkraUploader() {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select an image.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);

    try {
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        body: formData,
      });
      
      const data = await response.json();
      setPrediction(data);
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Failed to upload image.");
    }

    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center p-4">
      <h1 className="text-xl font-bold mb-4">Adinkra Symbol Recognition</h1>
      <input type="file" onChange={handleFileChange} className="mb-4" />
      <button
        onClick={handleUpload}
        className="px-4 py-2 bg-blue-500 text-white rounded"
        disabled={loading}
      >
        {loading ? "Uploading..." : "Upload and Predict"}
      </button>
      {prediction && (
        <div className="mt-4 p-4 border rounded">
          <p className="text-lg font-semibold">Prediction: {prediction.symbol}</p>
          {prediction.meaning && <p>Meaning: {prediction.meaning}</p>}
          <p>Confidence: {(prediction.confidence * 100).toFixed(2)}%</p>
        </div>
      )}
    </div>
  );
}