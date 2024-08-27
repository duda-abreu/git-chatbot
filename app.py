from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Carregando o modelo
model = joblib.load('git_chatbot_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data['question']
    answer = model.predict([question])[0]
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
