import math
from Distancia import *


class Silhouette(object):
	"""docstring for Silhouette"""
	def __init__(self,matrizDistancia,corpus):
		#super(Silhouette)._init_()
		self.matrizDistancia = matrizDistancia
		self.distancia = DistanciaEuclidiana()
		self.corpus = corpus
		self.matrizImprimir = []
		self.vetorPlot = [0]*len(self.corpus)
		self.vetorPlotVizinho = [0]*len(self.corpus)

	def distanciaGrupos(self):
		
		#entra na linha da matrizDistancia, cada linha é um grupo
		for grupoIndex, grupo in enumerate(self.matrizDistancia):
			print ("Grupo", grupoIndex)
			qntDados = 0
			distanciaGrupo = 0

			#atravessa todos dados do grupo, dadoIndex é o index do dado, 
			for dadoIndex, dado in enumerate(grupo):
				qntDados = 0
				distanciaGrupo = 0
				menorMedia = 10000
				
				if(dado != 0):
					for grupoIndex2, grupo2 in enumerate(self.matrizDistancia):
						if(dado != 0):
							#itera pelo grupo para calcular a distância
							distanciaGrupo = 0
							for dadoIndex2, dado2 in enumerate(grupo2):
								if(dado2 != 0):
									if(dadoIndex != dadoIndex2):
										qntDados += 1
										distanciaGrupo += self.distancia.calcula(self.corpus[dadoIndex],self.corpus[dadoIndex2])
							
							#calcula a media para o grupo do dado em questao
																	
							if (qntDados!=0 and grupoIndex2 == grupoIndex):
								mediaProprioGrupo = distanciaGrupo / qntDados

							if (qntDados!=0 and grupoIndex2 != grupoIndex):
								mediaOutroGrupo = distanciaGrupo / qntDados
								if(mediaOutroGrupo < menorMedia):
									menorMedia = mediaOutroGrupo
									self.vetorPlotVizinho[dadoIndex] = grupoIndex2

							qntDados = 0

					print("media proprio Grupo: ", mediaProprioGrupo)
					print("menor media outro grupo: ", menorMedia)
					desempenho = (menorMedia - mediaProprioGrupo) / max(menorMedia,mediaProprioGrupo)
					print(desempenho, "para dado ",dadoIndex)
					self.vetorPlot[dadoIndex] = desempenho
					print("\n")

	def plot(self, representacao=[]):
		file = open("Teste2.txt","w")
		file.write("                             0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1\n")
		file.write("                             0 0 0 1 1 2 2 2 3 3 4 4 4 5 5 6 6 6 7 7 8 8 8 9 9 0\n")
		file.write("                             0 4 8 2 6 0 4 8 2 6 0 4 8 2 6 0 4 8 2 6 0 4 8 2 6 0\n")
		file.write("Si     Clu    Viz    Dado    ++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
		file.write("                             +                                                  +\n")


		for grupoIndex, grupo in enumerate(self.matrizDistancia):

			for dadoIndex, dado in enumerate(grupo):
				if(dado != 0):
					desempenho = self.vetorPlot[dadoIndex]
					string = ("%0.3f    %s   %s   %10s  "%(desempenho, grupoIndex, self.vetorPlotVizinho[dadoIndex],representacao[dadoIndex][0]))
					string = str(string)
					file.write(string)
					if (desempenho < 0):
						file.write("**")
					while (desempenho > 0):
						desempenho = desempenho - 0.04
						file.write("**")
					file.write("\n")
						

					
			file.write("                         +                                                    +\n")

#sil = Silhouette(matrix,cor)
#sil.distanciaGrupos()
#sil.plot()