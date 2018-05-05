from bs4 import BeautifulSoup
import csv

# padrao de nome dos arquivos do banco de dados
FILE_NAME_PATTERN = "reut2-{0}.sgm"

# arquivo csv do dataset
dataset = open('dataset_reuters.csv', 'w', encoding = 'utf-8')
escritor = csv.writer(dataset)
escritor.writerow(['id_noticia','titulo_noticia', 'topicos', 'lugares', 'conteudo'])

# para cada arquivo, coleta o conteudo do body
# das noticias e concatena no arquivo CSV
id_new = 0
for i in range(22):
    # define o nome do arquivo
    file_number = ('%03d' % i)
    file_name = FILE_NAME_PATTERN.format(file_number)
    # abrir arquivo
    file = open(file_name, 'r')
    # le o conteudo do arquivo
    file_content = file.read()
    # monta arvore de tags
    tree_tags = BeautifulSoup(file_content, 'html.parser')
    # obtem cada noticia
    news = tree_tags.find_all('reuters')
    for new in news:
        
        topicos = new.find('topics')
        lista_topicos = topicos.find_all('d')
        s_topico = []
        for topico in lista_topicos:
            s_topico.append(topico.get_text())
        topicos = ",".join(topico for topico in s_topico)
            
        lugares = new.find('places')
        lista_lugares = lugares.find_all('d')
        s_lugares = []
        for lugar in lugares:
            s_lugares.append(lugar.get_text())
        lugares = ",".join(lugar for lugar in s_lugares)
    
        try: titulo = new.find('title').get_text()
        except: titulo = 'NA'
        try: conteudo = new.find('body').get_text()
        except: conteudo = 'NA'
        escritor.writerow([id_new, titulo, topicos, lugares, conteudo])        
        id_new = id_new + 1
    print("{0} terminado.".format(file_name))

# fecha arquivo dataset
dataset.close()
    