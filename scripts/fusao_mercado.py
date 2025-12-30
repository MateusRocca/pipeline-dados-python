from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'    

# Extract

dados_empresaA = Dados(path_json, 'json')
print('---------- Empresa A ----------')
print(f'Dados da empresa A (Arquivo JSON)\n{dados_empresaA.nome_colunas}')
print(f'Quantidade de linhas arquivo A: {dados_empresaA.qtd_linhas}')
dados_empresaB = Dados(path_csv, 'csv')
print('\n---------- Empresa B ----------')
print(f'Dados empresa B (Arquivo CSV - Ainda não renomeado)\n{dados_empresaB.nome_colunas}')
print(f'Quantidade de linhas arquivo B: {dados_empresaB.qtd_linhas}')


# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(f'Dados empresa B renomeados:\n{dados_empresaB.nome_colunas}')

dados_combinados = Dados.join(dados_empresaA, dados_empresaB)
print(dados_combinados.nome_colunas)
print(dados_combinados.qtd_linhas)

# Load
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_combinados.salvando_dados(path_dados_combinados)
print(path_dados_combinados)