import re
import nltk
from nltk import SnowballStemmer
from nltk.corpus import stopwords
nltk.download("stopwords")

class PreProcessor(object):
    
    #Construtor com nGrama = 1 como default.
    def __init__(self, nGrama = 1):
        super(PreProcessor, self).__init__()
        self.nGrama = nGrama

    #Retorna o texto inteiro em letra minuscula.
    def foldCase(sentence):
        sentence = sentence.replace("US", "UnitedStates")
        return sentence.lower()

    #Retorna uma lista de tokens (mantem tokens repetidas).
    def tokenize(sentence):
        sentence = sentence.replace("-","")
        sentence = sentence.replace("_","")
        regExpr = "[^a-zA-Z_]"
        return list(filter(lambda x: len(x) > 1, re.split(regExpr, sentence)))

    def process(self, listOfTokens = []):
        pass

class StopWords(PreProcessor):
    
    #Construtor.
    def __init__(self):
        PreProcessor.__init__(self)
    
    #Remove os "Stop Words" das lista de tokens (sem tokens repetidos).
    def process(self, listOfTokens = []):
        listOfStopWords = stopwords.words("english")
        return [token for token in listOfTokens if token not in listOfStopWords]

class Stemmer(PreProcessor):
    
    #Construtor.
    def __init__(self):
        PreProcessor.__init__(self)

    #Aplica stemizacao na lista de tokens.
    def process(self, listOfTokens = []):
        stemmer = SnowballStemmer("english")
        return [stemmer.stem(token) for token in listOfTokens]

class NGrama(PreProcessor):
    
    #Construtor com nGrama = n.
    def __init__(self, nGrama):
        PreProcessor.__init__(self)
        self.nGrama = nGrama
    
    #Retorna uma lista com n-gramas (termos compostos por n palavras).
    def process(self, listOfTokens = []):
        listOfGrams = []
        i = 0
        while i < (len(listOfTokens) - (self.nGrama) + 1):
            j = 0
            while j < self.nGrama:
                if (j == 0):
                    token = listOfTokens[i + j]
                else:
                    token = token + "_" + listOfTokens[i + j]
                j = j + 1
            listOfGrams.append(token)
            i = i + 1
        return listOfGrams
