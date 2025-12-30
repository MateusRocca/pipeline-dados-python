import json
import csv

class Dados:

    def __init__(self, path, tipo_dados):
        self.__path = path
        self.__tipo_dados = tipo_dados
        self.dados = self.__leitura_dados()
        self.nome_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()

    # Métodos de leitura são detalhes internos
    def __leitura_json(self):
        dados_json = []
        with open(self.__path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def __leitura_csv(self):
        dados_csv = []
        with open(self.__path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    def __leitura_dados(self):
        dados = []
        if self.__tipo_dados == 'json':
            dados = self.__leitura_json()
        
        elif self.__tipo_dados == 'csv':
            dados = self.__leitura_csv()

        elif self.__tipo_dados == 'list':
            dados = self.__path
            self.__path = 'lista em memoria'
        return dados
    
    # Auxiliares internos para o construtor
    def __get_columns(self):
        return list(self.dados[-1].keys())
    
    def __size_data(self):
        return len(self.dados)
    
    # MÉTODOS PÚBLICOS (Interface com o usuário)
    def rename_columns(self, key_mapping):
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
            
        self.dados = new_dados
        self.nome_colunas = self.__get_columns()
    
    
    @staticmethod
    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        return Dados(combined_list, 'list')
    

    def __transformando_dados_tabela(self):
        """Prepara os dados para o formato de lista de listas (CSV)."""
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponível'))
            dados_combinados_tabela.append(linha)
        
        return dados_combinados_tabela
    
    
    def salvando_dados(self, path):  

        dados_combinados_tabela = self.__transformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)