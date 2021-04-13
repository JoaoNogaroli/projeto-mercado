from flask import Flask, jsonify, render_template
import os
import pandas as pd
from datetime import datetime
import time
import MetaTrader5 as mt5

app=Flask(__name__)
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def index():
    if not mt5.initialize():
        print("Falha ao inicializar")
        mt5.shutdown()

    ativos=mt5.symbols_get()
    data=[]
    for i in range(0, 10):
       data.append(ativos[i].name)
    return render_template('index.html', data=data)



if __name__ == '__main__':
    app.run(debug=True, port=port)