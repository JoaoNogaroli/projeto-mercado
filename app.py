from inicializacao import app, db
from flask import Flask, jsonify, render_template, session
import os
import pandas as pd
from datetime import datetime
import time
from random import *
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from classe_modelo import Info


port = int(os.environ.get('PORT', 5000))



@app.route('/')
def index():
    headers = ['Abertura','Máxima','Mínima','Fechamento','tick_volume','hora','minuto']
    return render_template('index.html',headers=headers)

@app.route('/pegar', methods=['POST'])
def pegar():
    data = str(randint(1,100))
    tabela_info = db.Table('info',db.metadata)
    todos = db.session.query(tabela_info).all()
    result_dict = [u._asdict() for u in db.session.query(tabela_info).all()]

    '''for item in todos:
        print(type(item))'''
    lista = []
    for i in range(0, 6):
        lista.append(result_dict[i])
    #print(lista)
    #['id'],['open'],['high'],['low'],['close'],['tick_volume'],['hora'],['minuto']
    colunas = ['valores1','valores2','valores3','valores4','valores5','valores6','valores7']
    dici = dict(zip(colunas,lista))
    print(dici)
    return dici

if __name__ == '__main__':
    app.run(debug=True, port=port)