import pandas as pd

# Carrega o CSV
df = pd.read_csv('git_faq.csv', delimiter=',', quotechar='"')

# Verifica o conteúdo
print(df.head())

# Verifica e remove duplicatas
df = df.drop_duplicates()

# Verifica as classes na coluna 'answer'
print(df['answer'].value_counts())

# Salva o DataFrame
df.to_csv('processed_git_faq.csv', index=False)
