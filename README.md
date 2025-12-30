---Pipeline de Dados: Integração de Vendas (Pure Python Approach)---
Este projeto é um pipeline de ETL (Extract, Transform, Load) desenvolvido para consolidar bases de dados de diferentes formatos (JSON e CSV).

O grande diferencial deste projeto é o uso exclusivo de Python Nativo. Ao optar por não utilizar bibliotecas de alto nível como o Pandas,
este pipeline demonstra o domínio sobre lógica de programação, manipulação de estruturas de dados complexas e o funcionamento interno dos processos de engenharia de dados.

--Por que Python Nativo e não Pandas?--
Em um cenário de Engenharia de Dados, entender o "baixo nível" é fundamental para:

Otimização de Memória: Controle total sobre como cada linha de dado é carregada.

Entendimento da Lógica: Implementação manual de algoritmos de mapping e join.

Ambientes Restritos: Capacidade de rodar scripts em servidores onde não é possível instalar bibliotecas externas.

Fundamentos de POO: Aplicação real de classes, métodos privados e decoradores.

--Detalhes Técnicos e Lógica Aplicada--
1. Extração Customizada
Utilizei os módulos json e csv nativos. A leitura do CSV é feita via csv.DictReader, o que transforma cada linha em um dicionário,
facilitando a manipulação das colunas como pares chave-valor.

3. Transformação e Mapeamento
A lógica de renomeação de colunas foi implementada manualmente percorrendo listas de dicionários e reconstruindo as chaves com base em um key_mapping.

Desafio: Unificar nomes como "Nome do Item" e "Nome do Produto" sem usar métodos prontos de rename.

3. Implementação do "Join" Manual
O método join foi construído como um @staticmethod que recebe dois objetos da classe e estende as listas de dados, criando uma nova instância consolidada.

Tratamento de Dados Ausentes: Implementei uma lógica que percorre as colunas e, caso uma informação não exista em uma das fontes, preenche automaticamente com "Indisponível".

4. Carga (Load) Estruturada
Conversão de uma lista de dicionários para uma lista de listas para viabilizar a gravação via csv.writer, garantindo que o cabeçalho seja a primeira linha do arquivo final.

--Organização do Projeto--
Plaintext

pipeline_dados/
├── data_raw/               # Dados brutos de entrada
├── data_processed/         # Resultado final da integração
├── scripts/                # Script principal de execução
├── processamento_dados/    # Classes e métodos nativos
└── .gitignore              # Configurado para ignorar .venv e arquivos pesados

--Como Executar (Ambiente WSL/Ubuntu)--
Clone o repositório:

Bash

git clone git@github.com:MateusRocca/pipeline_dados.git
Acesse a pasta e rode o script:

Bash

python3 scripts/main.py

--Sobre o Mim--
Graduado em Análise e Desenvolvimento de Sistemas em Guaxupé-MG. 
Focado em transição de carreira para Engenharia de Dados, com sólido conhecimento em lógica de programação e arquitetura de sistemas no ambiente Linux (WSL).
