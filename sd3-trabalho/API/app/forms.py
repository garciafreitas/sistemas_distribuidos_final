from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField

class EscolhaCep(FlaskForm):
    cep = StringField(u'cep')
    submit = SubmitField('Pesquisar')

class Estacionamento(FlaskForm):
    vagas = open("./app/process/cidade.txt", 'r').readlines()
    modelos =open("./app/process/modelo.txt", 'r').readlines()
    choicesvaga = []
    choicesmodelo = []
    for i in vagas:
        vaga = (i.rstrip('\n'),i)
        choicesvaga.append(vaga)
    vaga = SelectField (u'vaga',choices=choicesvaga)
    # modelo = StringField('modelo')
    # placa = StringField('placa')
    submit = SubmitField('Enviar')
    
    for i in modelos:
        modelo = (i.rstrip('\n'),i)
        choicesmodelo.append(modelo)
    modelo = SelectField (u'modelo',choices=choicesmodelo)
    submit = SubmitField('Enviar')        