from flask import Flask, jsonify, render_template, request, session
import google.generativeai as genai
from api import Gemini_API_KEY as api



genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


chat_history = []

@app.route('/')
def index():
    return render_template('chat.html', chat_history=chat_history)

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        user_input = request.json.get('user_input')

        if user_input:
            response = chat.send_message(user_input)
            chat_history.append({"user": user_input, "bot": response.text})
            return jsonify({"response": response.text})
        else:
            return jsonify({"error": "No user input provided."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

