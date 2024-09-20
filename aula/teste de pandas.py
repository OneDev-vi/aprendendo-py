import pandas as pd

# Criar um DataFrame
data = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}
df = pd.DataFrame(data)

# Salvar o DataFrame como um arquivo Excel
df.to_excel('meu_arquivo.xlsx', index=False, engine='openpyxl')

print("Arquivo Excel criado com sucesso!")
