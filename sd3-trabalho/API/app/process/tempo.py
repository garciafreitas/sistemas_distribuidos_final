import random
from datetime import date
def previsao(vaga,modelo,placa):
    vagas = open("app\process\cidade.txt", 'a').readlines()

    if (vaga+'\n' + modelo+'\n'+'\n'+placa) in vagas:
        resultado = [{
            'vaga':  vaga,
            'modelo': modelo,
            'placa':  placa


        }]
        print(vaga)
        print(modelo)
        print(placa)
        return resultado
    return None


