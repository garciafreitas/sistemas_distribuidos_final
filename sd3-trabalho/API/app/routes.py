from flask import jsonify, render_template, flash

from app import app
from app.forms import Estacionamento, EscolhaCep
from app.process.openWearther import busca
from app.process.tempo import previsao
from app.process.equipamento import equipamento


## def index vai carregar uma pagina html
@app.route('/')
@app.route('/index') 
def index():                
    return render_template('index.html')
## estacionamento vai recebe o nome da cidade  e vai retorna as informaçoes 
@app.route('/estacionamento', methods=['GET','POST'])
def estacionamento():
    form = Estacionamento() #pega as informaçoes do arquivo forms.py e retorna a cidade escolhida
    if form.validate_on_submit():#verifica se tem informaçoes no formulario
        cidade = form.cidade.data #pega a string do nome da cidade que veio do formulario
        previsao_infos = previsao(cidade) # passa o nome da cidade pro tempo.py e retorna as informaçoes do json 
        return render_template('previsao.html', previsao_infos=previsao_infos) # vai renderizar as informaçoes do html com o json 
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


@app.route('/tempo/<cidade>', methods = ['GET'])
def tempo(cidade):                
    resultado = previsao(cidade)
    if resultado == None:
        return 'Cidade incorreta'
    return jsonify(resultado)
