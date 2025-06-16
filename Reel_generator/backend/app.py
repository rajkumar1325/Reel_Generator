import cohere #for txt generation
from flask import Flask, request, jsonify
from flask_cors import CORS

# accessing api from .env file
from dotenv import load_dotenv
import os

app = Flask(__name__) #flask app instance
CORS(app) # enable CORS for the app

load_dotenv()  #Load environment variables from .env file


COHERE_API_KEY = os.getenv("COHERE_API_KEY")    ## Get API key
co = cohere.Client(COHERE_API_KEY)  #Initialize Cohere client

#Defines a POST API endpoint at /generate.
@app.route('/generate', methods=['POST'])

def generate_reel(): #this fn runs when the endpoint hits
    data = request.get_json()   #Get JSON input from user
    prompt = data.get('prompt', '')     # Extract 'prompt' from JSON

    if not prompt:
        return jsonify({'status': 'error', 'message': 'No prompt provided.'}), 400

    try:

        response = co.generate(
        model='command',    ## Cohere's model name

        prompt=f"""Write a complete Instagram reel script that lasts 30 to 60 seconds on the topic:{prompt}.
        Start with an attention-grabbing hook, provide informative or entertaining middle content, and end with a strong call-to-action or question.
        Include possible visual suggestions or background sound ideas if relevant.""",

        max_tokens=500  #word token limit
)

            
        # Extracts the generated text from the first response and removes extra whitespace.
        generated_text = response.generations[0].text.strip()

        #Returns the script as a JSON response.
        return jsonify({'status': 'success', 'script': generated_text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
