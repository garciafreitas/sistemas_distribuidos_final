import random
from datetime import date
def previsao(vagas,modelos,vagasEmodelos):
    vagas = open("app\process\cidade.txt", 'r').readlines()
    modelos = open("app\process\modelo.txt", 'r').readlines()
    vagasEmodelos = open("app\process\cidadeEvagas.txt",'w').write(vagas,modelos)

    if (vagas+'\n' + modelos+'\n') in vagasEmodelos:
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

# def vagaAlocada(vaga,modelo,placa):
#     request = open('app\process\cidade.txt','r').readlines()
    
#     if(vaga+'&'+modelo+'&'+placa) in request:
#         vagaOcupada = [{
#             'vaga':vaga,
#             'modelo':modelo,
#             'placa':placa
#         }]
#         return vagaOcupada