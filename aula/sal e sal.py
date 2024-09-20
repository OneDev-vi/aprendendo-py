import pandas as pd

# Dados corrigidos
data = {
    "Nome da loja": ["Duas Torres Note America", "Duas Torres Note America"],  # Adicione o mesmo nome para todas as entradas
    "Localização": ["América do Norte", "Brasil"],  # Corrigido o nome da coluna
    "Data": ["11/09/2001", "11/09/2001"],
    "Clientes": ["Thiago S", "Vinicius Hr"],
    "Produto comprado": ["Sorvete e chocolate", "Manga, chocolate, danone grosso"],
    "Quantidade de Thiago S": ["1kg de sorvete e 500g de chocolate", None],  # Adicione None se não houver dados para o segundo cliente
    "Quantidade de Vinicius Hr": [None, "750g de danone, 500g de manga, 550g de chocolate, 350g de danone"],  # Adicione None para o cliente Thiago
    "Valor total": ["50 dólares", "70 reais"]  # Corrigido o formato
}

# Criar DataFrame
df = pd.DataFrame(data)

# Salvar como arquivo Excel
df.to_excel('Compras_de_2001.xlsx', index=False, engine='openpyxl')

print("Salvo com sucesso!!!")
