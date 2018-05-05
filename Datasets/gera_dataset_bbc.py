import os
import csv

BBC_FOLDERS_PATH = 'bbc/{0}'
BBC_FILES_PATH = 'bbc/{0}/{1}'

# cria arquivo csv e escritor
dataset = open('dataset_bbc.csv', 'w', encoding = 'utf-8')
escritor = csv.writer(dataset)
escritor.writerow(['conteudo', 'categoria'])

# obter o nome das pastas
categorias = os.listdir('bbc')

for categoria in categorias:
    # listar todos os textos daquela categoria
    for documento in os.listdir(BBC_FOLDERS_PATH.format(categoria)):
        # abre arquivo
        doc_file = open(BBC_FILES_PATH.format(categoria, documento), 'r')
        # pega conteudo do arquivo
        texto_documento = doc_file.read()
        # escreve no arquivo dataset csv
        escritor.writerow([texto_documento, categoria])
    print("categoria [{0}] terminada.".format(categoria))
    
# fecha o arquivo csv
dataset.close()
