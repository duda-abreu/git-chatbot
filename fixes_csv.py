import pandas as pd

# Crrigir a formatação do CSV
def correct_csv_format(input_file, output_file):
    try:
        # Ler o CSV com o delimitador e caractere de citação
        df = pd.read_csv(input_file, delimiter=',', quotechar='"', escapechar='\\', skipinitialspace=True)
        
        # Verifica o DataFrame para ver como os dados estão sendo lidos
        print("DataFrame after loading:")
        print(df.head())

        # Remove aspas e espaços desnecessários
        df['answer'] = df['answer'].str.strip().str.replace('""', '"', regex=False)
        
        # Verifica e remove duplicatas
        df = df.drop_duplicates()

        # Salvar o DataFrame
        df.to_csv(output_file, index=False)
        print(f"Processed CSV saved to {output_file}")
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Corrige o CSV
correct_csv_format('git_faq.csv', 'processed_git_faq.csv')
