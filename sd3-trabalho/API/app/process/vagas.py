def list_vagas(vaga):
        vagas = open("./app/process/cidade.txt", 'r').readlines()
        if (vaga+'\n') in vagas:
                dados = [{
                'vaga':vaga,
                # 'modelo':modelo,
                # 'placa':placa
            }]
                return dados
        return None