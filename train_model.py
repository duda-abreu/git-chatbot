import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import joblib

# Carrega e prepara os dados
data = pd.read_csv('processed_git_faq.csv')
X = data['question']
y = data['answer']

# Divide os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cria o pipeline
pipeline = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression()
)

# Treina o modelo
pipeline.fit(X_train, y_train)

# Avalia o modelo
accuracy = pipeline.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Salva
joblib.dump(pipeline, 'git_chatbot_model.pkl')
