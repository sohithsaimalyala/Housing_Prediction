from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import threading

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
    return {"message": "Hello, FastAPI running with threading!"}

# Define the predict endpoint
@app.post("/predict")
def predict(data: YourInputModel):
    prediction = (data.size * 1000) + (data.rooms * 500)
    return {
        "input": {
            "size": data.size,
            "rooms": data.rooms,
            "location": data.location
        },
        "prediction": prediction
    }

# Function to start the FastAPI server in a separate thread
def start_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Start the server in a separate thread
thread = threading.Thread(target=start_server, daemon=True)
thread.start()
