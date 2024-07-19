import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging
import traceback
import textwrap

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
openai.api_base = "https://chatapi.akash.network/api/v1"  # Update if needed

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    logger.debug(f"Received message: {user_message}")
    
    try:
        # Create a chat completion using the provided method
        client = openai.OpenAI(api_key=api_key, base_url=openai.api_base)
        response = client.chat.completions.create(
            model="llama3-8b",  # Replace with the appropriate model
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        
        # Access the response attributes correctly
        reply = response.choices[0].message.content  # Access `content` attribute correctly
        formatted_reply = textwrap.fill(reply, 50)  # Format the reply for readability
        
        logger.debug(f"Response from OpenAI: {formatted_reply}")
        return jsonify(formatted_reply)
    except Exception as e:
        # General error handling with detailed logging
        logger.error(f"Unexpected error: {str(e)}\n{traceback.format_exc()}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Adjust the port as needed
