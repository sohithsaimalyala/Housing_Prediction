{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
from fastapi import FastAPI

# Create the FastAPI app instance
app = FastAPI()

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}

# Add other endpoints as needed
@app.get("/hello")
def say_hello():
    return {"greeting": "Hello, World!"}
