import csv
import os
import pandas
from Representation import Binary
from Representation import TFNorm
from Representation import TFIDFNorm

#Carrega o conteudo do corpora na memoria.
def loadCorpus(sourcepath):
    corpus = {}
    csvFile = pandas.read_csv(sourcepath)
    corpus["document"] = []
    for sentence in csvFile.values.tolist():
        corpus["document"].append(sentence[0].strip())    
    return corpus

def matrixToCsv(nome, matrix):
    csvFile = open("C:/Users/Anderson/Desktop/Trabalhos/IA/Output/" + nome + ".csv", "w", newline = "")
    writer = csv.writer(csvFile)
    writer.writerows(matrix)
    csvFile.close()
    pass

def corpusToTxt(nome, content):
    txtFile = open("C:/Users/Anderson/Desktop/Trabalhos/IA/Output/" + nome + ".txt", "w", newline = "")
    document = 0
    while(document < len(content)):
        token = 0
        sentence = content[document]
        txtFile.write("{}. ".format(document))
        while (token < len(sentence)):
            if(token == len(sentence) - 1):
                txtFile.write(sentence[token] + ".")
            else:
                txtFile.write(sentence[token] + ", ")
            token = token + 1
        if(document < len(content) - 1):
            txtFile.write("\n\n")
        document = document + 1
    txtFile.close()
    pass

def termsToTxt(nome, content):
    txtFile = open("C:/Users/Anderson/Desktop/Trabalhos/IA/Output/" + nome + ".txt", "w", newline = "")
    token = 0
    while(token < len(content)):
        if(token == len(content) - 1):
            txtFile.write("{}. ".format(token) + content[token] + ".")
        else:
            txtFile.write("{}. ".format(token) + content[token] + ",\n")
        token = token + 1
    txtFile.close()
    pass

def main():
    
    #Carregando o corpus.
    cut = "_0.05"
#    sourcepathI = os.path.join("C:/Users/Anderson/Desktop/Trabalhos/IA/Input/", "bbc_input_final.csv")
#    sourcepathII = os.path.join("C:/Users/Anderson/Desktop/Trabalhos/IA/Input/", "reuters_input_final.csv")
#    corpusI = loadCorpus(sourcepathI)
#    corpusII = loadCorpus(sourcepathII)
#    
#    #BBC: instanciando as representacoes, salvando matriz, corpus e lista de termos.
#    binaryBBC101 = Binary(corpusI, [1, 0, 1])
#    matrixToCsv("bbc_binary_101" + cut, binaryBBC101.getMatrix())
#    corpusToTxt("bbc_corpus_101", binaryBBC101.getCorpus())
#    termsToTxt("bbc_terms_101" + cut, binaryBBC101.getListOfTerms())
#    print("Representation Created." + "\n")
#    binaryBBC102 = Binary(corpusI, [1, 0, 2])
#    matrixToCsv("bbc_binary_102" + cut, binaryBBC102.getMatrix())
#    corpusToTxt("bbc_corpus_102", binaryBBC102.getCorpus())
#    termsToTxt("bbc_terms_102" + cut, binaryBBC102.getListOfTerms())
#    print("Representation Created." + "\n")
#    binaryBBC111 = Binary(corpusI, [1, 1, 1])
#    matrixToCsv("bbc_binary_111" + cut, binaryBBC111.getMatrix())
#    corpusToTxt("bbc_corpus_111", binaryBBC111.getCorpus())
#    termsToTxt("bbc_terms_111" + cut, binaryBBC111.getListOfTerms())
#    print("Representation Created." + "\n")
#    binaryBBC112 = Binary(corpusI, [1, 1, 2])
#    matrixToCsv("bbc_binary_112" + cut, binaryBBC112.getMatrix())
#    corpusToTxt("bbc_corpus_112", binaryBBC112.getCorpus())
#    termsToTxt("bbc_terms_112" + cut, binaryBBC112.getListOfTerms())
#    print("Representation Created." + "\n")
#    tfNormBBC101 = TFNorm(corpusI, [1, 0, 1])
#    matrixToCsv("bbc_tf_101" + cut, tfNormBBC101.getMatrix())
#    print("Representation Created." + "\n")
#    tfNormBBC102 = TFNorm(corpusI, [1, 0, 2])
#    matrixToCsv("bbc_tf_102" + cut, tfNormBBC102.getMatrix())
#    print("Representation Created." + "\n")
#    tfNormBBC111 = TFNorm(corpusI, [1, 1, 1])
#    matrixToCsv("bbc_tf_111" + cut, tfNormBBC111.getMatrix())
#    print("Representation Created." + "\n")
#    tfNormBBC112 = TFNorm(corpusI, [1, 1, 2])
#    matrixToCsv("bbc_tf_112" + cut, tfNormBBC112.getMatrix())
#    print("Representation Created." + "\n")
#    tfIdfNormBBC101 = TFIDFNorm(corpusI, [1, 0, 1])
#    matrixToCsv("bbc_tfidf_101" + cut, tfIdfNormBBC101.getMatrix())
#    print("Representation Created." + "\n")
#    tfIdfNormBBC102 = TFIDFNorm(corpusI, [1, 0, 2])
#    matrixToCsv("bbc_tfidf_102" + cut, tfIdfNormBBC102.getMatrix())
#    print("Representation Created." + "\n")
#    tfIdfNormBBC111 = TFIDFNorm(corpusI, [1, 1, 1])
#    matrixToCsv("bbc_tfidf_111" + cut, tfIdfNormBBC111.getMatrix())
#    print("Representation Created." + "\n")
#    tfIdfNormBBC112 = TFIDFNorm(corpusI, [1, 1, 2])
#    matrixToCsv("bbc_tfidf_112" + cut, tfIdfNormBBC112.getMatrix())
#    print("Representation Created." + "\n")
#    
#    #Reuters: instanciando as representacoes, salvando matriz, corpus e lista de termos.
#    binaryReuters101 = Binary(corpusII, [1, 0, 1])
#    matrixToCsv("reuters_binary_101" + cut, binaryReuters101.getMatrix())
#    corpusToTxt("reuters_corpus_101", binaryReuters101.getCorpus())
#    termsToTxt("reuters_terms_101" + cut, binaryReuters101.getListOfTerms())
#    print("Representation Created." + "\n")
#    binaryReuters102 = Binary(corpusII, [1, 0, 2])
#    matrixToCsv("reuters_binary_102" + cut, binaryReuters102.getMatrix())
#    corpusToTxt("reuters_corpus_102", binaryReuters102.getCorpus())
#    termsToTxt("reuters_terms_102" + cut, binaryReuters102.getListOfTerms())
#    print("Representation Created." + "\n")
#    binaryReuters111 = Binary(corpusII, [1, 1, 1])
#    matrixToCsv("reuters_binary_111" + cut, binaryReuters111.getMatrix())
#    corpusToTxt("reuters_corpus_111", binaryReuters111.getCorpus())
#    termsToTxt("reuters_terms_111" + cut, binaryReuters111.getListOfTerms())
#    print("Representation Created." + "\n")
#    binaryReuters112 = Binary(corpusII, [1, 1, 2])
#    matrixToCsv("reuters_binary_112" + cut, binaryReuters112.getMatrix())
#    corpusToTxt("reuters_corpus_112", binaryReuters112.getCorpus())
#    termsToTxt("reuters_terms_112" + cut, binaryReuters112.getListOfTerms())
#    print("Representation Created." + "\n")
#    tfNormReuters101 = TFNorm(corpusII, [1, 0, 1])
#    matrixToCsv("reuters_tf_101" + cut, tfNormReuters101.getMatrix())
#    print("Representation Created." + "\n")
#    tfNormReuters102 = TFNorm(corpusII, [1, 0, 2])
#    matrixToCsv("reuters_tf_102" + cut, tfNormReuters102.getMatrix())
#    print("Representation Created." + "\n")
#    tfNormReuters111 = TFNorm(corpusII, [1, 1, 1])
#    matrixToCsv("reuters_tf_111" + cut, tfNormReuters111.getMatrix())
#    print("Representation Created." + "\n")
#    tfNormReuters112 = TFNorm(corpusII, [1, 1, 2])
#    matrixToCsv("reuters_tf_112" + cut, tfNormReuters112.getMatrix())
#    print("Representation Created." + "\n")
#    tfIdfNormReuters101 = TFIDFNorm(corpusII, [1, 0, 1])
#    matrixToCsv("reuters_tfidf_101" + cut, tfIdfNormReuters101.getMatrix())
#    print("Representation Created." + "\n")
#    tfIdfNormReuters102 = TFIDFNorm(corpusII, [1, 0, 2])
#    matrixToCsv("reuters_tfidf_102" + cut, tfIdfNormReuters102.getMatrix())
#    print("Representation Created." + "\n")
#    tfIdfNormReuters111 = TFIDFNorm(corpusII, [1, 1, 1])
#    matrixToCsv("reuters_tfidf_111" + cut, tfIdfNormReuters111.getMatrix())
#    print("Representation Created." + "\n")
#    tfIdfNormReuters112 = TFIDFNorm(corpusII, [1, 1, 2])
#    matrixToCsv("reuters_tfidf_112" + cut, tfIdfNormReuters112.getMatrix())
#    print("Representation Created." + "\n")
    
    #Instancia de teste.
    sourcepath0 = os.path.join("C:/Users/Anderson/Desktop/Trabalhos/IA/Corpus/Teste/", "TesteI.csv")
    corpus0 = loadCorpus(sourcepath0)
    binaryTest = Binary(corpus0, [1, 1, 1])
    matrixToCsv("test_binary" + cut, binaryTest.getMatrix())
    corpusToTxt("test_corpus", binaryTest.getCorpus())
    termsToTxt("test_terms" + cut, binaryTest.getListOfTerms())

main()