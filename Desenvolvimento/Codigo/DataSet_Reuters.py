import csv
import os
import pandas
#from bs4 import BeautifulSoup

def Reuters():
    corpus = os.listdir("C:/Users/Anderson/Desktop/Trabalhos/IA/Corpus/Reuters 21578 (NLTK)/reuters")
    csvFile = open("reuters.csv", "w", encoding = "utf-8", newline = '')
    writer = csv.writer(csvFile)
    writer.writerow(["<text>"])
    for folder in corpus:
        subfolder = os.listdir(folder)
        for file in subfolder:
            sentence = open(folder + "/" + file, "r")
            content = sentence.read()
            if (len(content) > 250):
                writer.writerow([content])
    csvFile.close()
    dataSet = pandas.read_csv("reuters.csv")
    dataSet.to_csv("reuters_input.csv", index = False)
    pass
    
    #Código para carregar, anterior.
    '''for row in corpus:
        sentence = open(row, "r")
        content = sentence.read()
        bs = BeautifulSoup(content, "lxml")
        listOfTexts = bs.findAll("text")
        for text in listOfTexts:
            writer.writerow([text.get_text()])
    csvFile.close()
    dataSet = pandas.read_csv("reuters.csv")
    dataSet.to_csv("reuters_input.csv", index = False)
    pass'''

Reuters()
