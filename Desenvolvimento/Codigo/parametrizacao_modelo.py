"""
exemplo de
arquivos de configuracao
"""
PARAM_CODIFICATION = "{0}{1}{2}"

class Representacao():
    def __init__(self, params):
        stopwords, stem, ngrams = params
        
        print("Representacao running for {0} params.".format(params))
        print("Represetacao save config in dataset_{0}.csv".format(PARAM_CODIFICATION.format(int(stopwords), int(stem), ngrams)))
        print('...')

# ordem = stopwords, stemmer, ngramas
configs = [{'config_101':[True,  False,  1]},
           {'config_102':[True,  False,  2]},
           {'config_103':[True,  False,  3]},
           {'config_001':[False, False,  1]},
           {'config_002':[False, False,  2]},
           {'config_003':[False, False,  3]},
           {'config_011':[False, True,   1]},
           {'config_012':[False, True,   2]},
           {'config_013':[False, True,   1]},
           {'config_111':[True,  True,   1]},
           {'config_112':[True,  True,   2]},
           {'config_113':[True,  True,   3]},]

for config in configs:
    for config_name in config:
        Representacao(config[config_name])
       
