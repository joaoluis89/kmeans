import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Distancia import *
from Representation import *
from threading import Thread
from Silhouette import *
from threading import Thread

class Kmeans(object):
    """docstring for Kmeans"""
    def __init__(self, numberOfCentroids, representacao=None, distancia=None, corpus=None):
        super(Kmeans).__init__()
        self.numberOfCentroids = numberOfCentroids
        if (corpus is not None):
            self.representacao = corpus
        elif (representacao is not None):
            self.representacao = representacao.getMatrix()
        else:
            raise ValueError("Nao foi informado nem uma representacao, nem um corpus ja tratado, por favor informe")

        """self.representacao = np.array("""
        """    ["""
        """        [3,2,1],"""
        """        [3,4,5],"""
        """        [2,8,7],"""
        """        [3,2,9]"""
        """    ]"""
        """)"""
        self.distancia = distancia
        self.quantidadeDeDados = len(self.representacao)
        self.centroidsArray = self.defineCentroids()
        self.aprendizagem = math.inf

    def defineCentroids(self):
        """docstring for defineCentroids"""
        """self.numeroDimensoes = self.representacao.getNumeroDimensoes() """
        self.numeroDimensoes = len(self.representacao[0])
        """
        cria a matriz de centroids, onde as colunas (x) representam
        as n dimensoes e as linhas (y) representam os n centroids
        """
        centroidsArray = [
            [
                None for x in range(self.numeroDimensoes)
            ]
            for y in range(self.numberOfCentroids)
        ]

        for column in range(self.numeroDimensoes):
            for line in range(self.numberOfCentroids):
                dadoAleatorio = random.randint(0, (self.quantidadeDeDados - 1))
                centroidsArray[line][column] = self.representacao[dadoAleatorio][column]
        return centroidsArray


    def calculaProximidade(self):
        self.matrixEsparsa = np.zeros((self.numberOfCentroids, self.quantidadeDeDados))
        threads = []
       # print(self.representacao)
        for dadoIndex, dado in enumerate(self.representacao):
            thread = Thread(target=self.findCentroidMaisProximo, args=(dadoIndex, dado))
            thread.start()
            threads.append(thread)
        self.waitForThreads(threads)
        pass
        """adiconar em um vetor esparso"""

    def waitForThreads(self, threads = []):
        for thread in threads:
            thread.join()

    def findCentroidMaisProximo(self, dadoIndex, dado):
        (valorDistancia, centroidMenorIndice) = (math.inf, None)
        for centroidIndex, centroid in enumerate(self.centroidsArray):
            numberDistancia = self.distancia.calcula(centroid, dado)
            if (self.distancia.isMaisProximo(valorDistancia, numberDistancia)):
                (valorDistancia, centroidMenorIndice) = (numberDistancia, centroidIndex)
        self.matrixEsparsa[centroidMenorIndice][dadoIndex] = 1

    def atualizaCentroids(self):
        threads = []
        for centroidIndex in range(self.numberOfCentroids):
            thread = Thread(target = self.atualizaCentroid, args=(centroidIndex, ))
            thread.start()
            threads.append(thread)
        self.waitForThreads(threads)

    def atualizaCentroid(self, centroidIndex):
        vetorAtualizado = np.zeros(self.numeroDimensoes)
        quantidadeDeDados = 0
        for dadoIndex in range(self.quantidadeDeDados):
            if(self.matrixEsparsa[centroidIndex][dadoIndex]):
                vetorAtualizado += self.representacao[dadoIndex]
                quantidadeDeDados += 1
        vetorAtualizado = vetorAtualizado / quantidadeDeDados
        self.centroidsArray[centroidIndex] = vetorAtualizado

    def funcaoDeAprendizagem(self):
        aprendizagem = np.zeros(self.numberOfCentroids)
        threads = []
        for centroidIndex in range(self.numberOfCentroids):
            thread = Thread(target = self.funcaoDeAprendizagemAux, args = (centroidIndex, aprendizagem))
            thread.start()
            threads.append(thread)
        self.waitForThreads(threads)
        aprendizagem = np.sum(aprendizagem)
        return aprendizagem, aprendizagem == self.aprendizagem

    def funcaoDeAprendizagemAux(self, centroidIndex, vetorAprendizagemCentroids):
        for dadoIndex in range(self.quantidadeDeDados):
            if(self.matrixEsparsa[centroidIndex][dadoIndex]):
                vetorAprendizagemCentroids[centroidIndex] += self.distancia.calcula(self.representacao[dadoIndex], self.centroidsArray[centroidIndex])


    def aprenda(self, numeroCentroids=1, epocas=30):
        aprendizagemArray = np.zeros(epocas + 1)
        epocaArray = range(epocas + 1)
        for i in range(epocas):
            print("Calculando proximidade")
            self.calculaProximidade()
            print("Atualizando centroids")
            self.atualizaCentroids()
            print("Funcão de aprendizagem")
            (self.aprendizagem, convergiu) = self.funcaoDeAprendizagem()
            print(self.aprendizagem, convergiu)
            aprendizagemArray[i + 1] = self.aprendizagem
            if (convergiu):
                break

#corpus = pd.read_csv("../Output/bbc_binary_111_0.05.csv", header=None, encoding="latin_1")
corpus = np.loadtxt(open("../Output/bbc_binary_111_0.05.csv", "rb"), delimiter=",")
print(corpus)
kmeans = Kmeans(7, None, DistanciaEuclidiana(), corpus)
kmeans.aprenda(7)
# file = open("../Corpus/zoo.txt","r")
# kmeans = Kmeans(7, Zoo(file,(False,False,False)), DistanciaEuclidiana())
# kmeans.aprenda(7)

# ile = open("../Corpus/zoo.txt","r")

# #apenas para o Silhouette pegar os nomes dos animais
# matrix =[]
# for line in ile:
#     line = line[:-1]
#     linha = line.split(',')
#     matrix.append(linha)


sil = Silhouette(kmeans.matrixEsparsa,kmeans.representacao)
sil.distanciaGrupos()


sil.plot(matrix)
file.close()
