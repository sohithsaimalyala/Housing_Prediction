{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cee7aa8c-bdf9-4d5d-9810-020111632b26",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import requests\n",
    "\n",
    "# Define the backend FastAPI endpoint\n",
    "API_ENDPOINT = \"http://127.0.0.1:8000/predict\"  # Replace with your FastAPI deployment URL\n",
    "\n",
    "# App title\n",
    "st.title(\"Real-Time Classification with Deployed Model\")\n",
    "st.write(\"This app allows you to interact with the deployed model for real-time predictions.\")\n",
    "\n",
    "# Sidebar input form\n",
    "st.sidebar.header(\"Input Features\")\n",
    "st.sidebar.write(\"Provide the input features below:\")\n",
    "\n",
    "# Input fields based on FastAPI model\n",
    "size = st.sidebar.number_input(\"Property Size (Square Footage)\", value=1000.0)\n",
    "rooms = st.sidebar.number_input(\"Number of Rooms\", min_value=1, max_value=20, value=3)\n",
    "location = st.sidebar.selectbox(\"Location Type\", [\"Urban\", \"Suburban\", \"Rural\"])\n",
    "\n",
    "# Prepare the input for the API\n",
    "input_data = {\n",
    "    \"size\": size,\n",
    "    \"rooms\": rooms,\n",
    "    \"location\": location\n",
    "}\n",
    "\n",
    "# Show the input data\n",
    "st.subheader(\"Your Input Data\")\n",
    "st.json(input_data)\n",
    "\n",
    "# Button to make predictions\n",
    "if st.button(\"Get Prediction\"):\n",
    "    try:\n",
    "        # Send the data to the backend FastAPI\n",
    "        response = requests.post(API_ENDPOINT, json=input_data)\n",
    "        response.raise_for_status()  # Raise error for bad status codes\n",
    "\n",
    "        # Display prediction\n",
    "        prediction = response.json()\n",
    "        st.success(f\"Prediction: {prediction.get('prediction', 'Unknown')}\")\n",
    "        st.write(\"Details:\", prediction)\n",
    "\n",
    "    except requests.exceptions.RequestException as e:\n",
    "        st.error(f\"Error: {e}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
