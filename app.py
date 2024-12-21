from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import nest_asyncio
# Uncomment if using an ML model
# import joblib

# Create the FastAPI app
app = FastAPI()

# Define a Pydantic model for input validation
class YourInputModel(BaseModel):
    size: float  # Example: Square footage
    rooms: int   # Example: Number of rooms
    location: str  # Example: Urban, Suburban, etc.

# Uncomment and load your ML model if required
# model = joblib.load("model.pkl")

# Define the root endpoint
@app.get("/")
def read_root():
    """
    Root endpoint to verify the application is running.
    """
    return {"message": "Hello, FastAPI running in Jupyter!"}

# Define the predict endpoint
@app.post("/predict")
def predict(data: YourInputModel):
    """
    Prediction endpoint that accepts input data and returns a prediction.
    """
    # Example prediction logic
    # Replace this with your ML model logic if required
    # For ML models:
    # features = [[data.size, data.rooms, data.location_numeric]]
    # prediction = model.predict(features)

    # Placeholder logic for demonstration
    prediction = (data.size * 1000) + (data.rooms * 500)

    return {
        "input": {
            "size": data.size,
            "rooms": data.rooms,
            "location": data.location
        },
        "prediction": prediction
    }

# Allow running FastAPI in Jupyter Notebook
nest_asyncio.apply()

# Start the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
