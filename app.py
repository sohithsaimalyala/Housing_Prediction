from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import nest_asyncio

# Patch the existing event loop for Jupyter Lab compatibility
nest_asyncio.apply()

# Create the FastAPI app
app = FastAPI()

# Define a Pydantic model for input validation
class YourInputModel(BaseModel):
    size: float  # Example: Square footage
    rooms: int   # Example: Number of rooms
    location: str  # Example: Urban, Suburban, etc.

# Define the root endpoint
@app.get("/")
def read_root():
    """
    Root endpoint to verify the application is running.
    """
    return {"message": "Hello, FastAPI running in Jupyter Lab!"}

# Define the predict endpoint
@app.post("/predict")
def predict(data: YourInputModel):
    """
    Prediction endpoint that accepts input data and returns a prediction.
    """
    # Example prediction logic
    prediction = (data.size * 1000) + (data.rooms * 500)
    return {
        "input": {
            "size": data.size,
            "rooms": data.rooms,
            "location": data.location
        },
        "prediction": prediction
    }

# Start the FastAPI server
if __name__ == "__main__":
    # Use uvicorn to run the app inside Jupyter Lab
    uvicorn.run(app, host="127.0.0.1", port=8000)
