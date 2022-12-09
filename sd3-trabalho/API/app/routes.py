from flask import render_template

from app import app
from app.forms import Estacionamento, EscolhaCep
from app.process.request_correios import busca
from app.process.equipamento import equipamento
from app.process.vagas import list_vagas


## def index vai carregar uma pagina html
@app.route('/')
@app.route('/index') 
def index():                
    return render_template('index.html')
## estacionamento vai recebe o nome da cidade  e vai retorna as informaçoes 
@app.route('/estacionamento', methods=['GET','POST'])
def estacionamento():
    form = Estacionamento() #pega as informaçoes do arquivo forms.py e retorna a vaga escolhida
    
    if form.validate_on_submit():
        dados = lista_vagas
        vagaOcupada = form.vaga.data
        vagaModelo = form.modelo.data
        vagaPlaca = form.placa.data
        lista_vagas = list_vagas(vagaOcupada,vagaModelo,vagaPlaca)

        if dados.lower(vagaOcupada,vagaModelo,vagaPlaca) in lista_vagas:
            form.vaga.data = ""
            form.modelo.data = ""
            form.placa.data = ""
            print("Chegou ate aqui....")
            return render_template('estacionamentoOcupado.html', lista_vagas=lista_vagas) # vai renderizar as informaçoes do html com o json 
    else:
        print("azedou....")
    return render_template('estacionamento.html', form=form) #caso o form nao seja valido permanece na pagina estacionamento 

@app.route('/externa', methods=['GET','POST'])
def externa():
    form = EscolhaCep() #pega as informaçoes do arquivo forms.py e retorna a cidade escolhida
    if form.validate_on_submit():#verifica se tem informaçoes no formulario
        cep = form.cep.data
        cep =  busca(cep)
      
        return render_template('api_externa.html',cep=cep) 
    return render_template('correios.html', form=form)

@app.route('/outros', methods=['GET','POST'])
def outros(): #vai carregar os dados da api_externa 
    dados = equipamento()
    return render_template('api_outros.html', dados=dados) #renderizar a pagina 