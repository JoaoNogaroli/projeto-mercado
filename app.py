from inicializacao import app, db
from flask import Flask, jsonify, render_template, session,request
import os
import pandas as pd
from datetime import datetime
import time
from random import *
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from classe_modelo import Info

FORMAT = 'utf-8'

#socket
import socket

port = int(os.environ.get('PORT', 5000))

FORMAT = 'utf-8'


@app.route('/')
def index():
    headers = ['Abertura','Máxima','Mínima','Fechamento','tick_volume','hora','minuto']
    return render_template('index.html',headers=headers)

@app.route('/pegar', methods=['POST'])
def pegar():
   
    reply = request.get_data()
    reply = reply.decode(FORMAT)
    print("PEGANDO DO BROWSER: ",reply)
    

    time.sleep(2)
    HEADER = 64
    PORT = 5000

    DISCONNECT_MESSAGE = "!DISCONNECT"
    #name2 = 'ec2-18-228-155-48.sa-east-1.compute.amazonaws.com'
    #print("name2: ", name2)
    name3 = '18.228.155.48'
    #print('name3: ', name3)
    ADDR = (name3, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print("INICIANDO ")
    try:
        client.connect(ADDR)
        #print('Conectado')
    except socket.error as e:
        print("ERROR NO CONNECT")
        print(str(e))

    def send(msg):
        message = msg.encode(FORMAT)
        
        client.send(message)
        #print(client.recv(2048).decode(FORMAT))
    
    #print("Pronto! Envie sua mensagem")
    send(reply)

    time.sleep(4)

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
    #print(dici)

    return dici




if __name__ == '__main__':
    app.run(debug=True, port=port)