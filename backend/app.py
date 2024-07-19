import openai
import textwrap
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://chatapi.akash.network/api/v1"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = openai.Completion.create(
        model="llama3-8b",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )
    return jsonify(response.choices[0].message['content'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

