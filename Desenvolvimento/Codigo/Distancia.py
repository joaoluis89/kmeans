import math

class Distancia(object):
    """docstring for Distancia"""
    def __init__(self):
        pass
    """deve devolver um double com a distancia calculada"""

    def calcula(self, vetorDimensoes=[], centroidDimensoes=[]):
        pass

    def isMaisProximo(self, menor, distancia):
        pass


class DistanciaEuclidiana(Distancia):

    """Calcula distancia Euclidiana entre dois pontos"""
    def __init__(self):
        Distancia.__init__(self)

    def calcula(self, vetorDimensoes=[], centroidDimensoes=[]):
            distancia = math.sqrt(sum([(x-y)**2 for x, y in zip(vetorDimensoes,centroidDimensoes)]))
            return distancia

    def isMaisProximo(self, menor, distancia):
        if(distancia < menor):
            return True
        return False


class SemelhancaCossenos(Distancia):
    """Calcula a semelhanca de cossenos entre dois vetore"""
    def __init__(self):
        Distancia.__init__(self)

    def comprimento(vetor=[]):
        comp = math.sqrt(sum([(a)**2 for a in iter(vetor)]))
        return comp

    def calcula(self, vetorDimensoes=[], centroidDimensoes=[]):
        escalar = sum([(a*b) for a, b in zip (vetorDimensoes,centroidDimensoes)])
        comprimentoA = comprimento(vetorDimensoes)
        comprimentoB = comprimento(centroidDimensoes)
        cos = escalar / (comprimentoA * comprimentoB)
        return cos

    #Compara qual cosseno se aproximo mais de cos(0)
    def isMaisProximo(self, menor, distancia):
        if(distancia > menor):
            return True
        return False
