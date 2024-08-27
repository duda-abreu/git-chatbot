import joblib

# Carrega o modelo
model = joblib.load('git_chatbot_model.pkl')

# Função para fazer as previsões
def get_answer(question):
    return model.predict([question])[0]

# Testa com algumas perguntas
test_questions = [
    "How do you initialize a new Git repository?",
    "How do you merge branches?"
]

for question in test_questions:
    answer = get_answer(question)
    print(f"Question: {question}\nAnswer: {answer}\n")
