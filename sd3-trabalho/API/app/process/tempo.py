import random
from datetime import date
def previsao(vagas):
    vagas = open("app\process\vagas.txt", 'r').readlines()

    if (vagas+'\n') in vagas:
        resultado = [{
            'vaga': vagas,
            'modelo':((str.format)),
        }]
        return resultado
    return None

opcao = [
    'alocado',
    'livre',
]

def vagaAlocada(vaga,modelo,placa):
    request = open('app\process\vagas.txt','r').readlines()
    
    if(vaga+'&'+modelo+'&'+placa) in request:
        vagaOcupada = [{
            'vaga':vaga,
            'modelo':modelo,
            'placa':placa
        }]
        return vagaOcupada