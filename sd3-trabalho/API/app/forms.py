from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

class EscolhaCep(FlaskForm):
    cep = StringField(u'cep')
    submit = SubmitField('Pesquisar')

class Estacionamento(FlaskForm):
    vaga = StringField(label='Vaga')
    modelo =StringField(label='Modelo')
    placa = StringField(label='Placa')
    submit =SubmitField(label='Enviar')