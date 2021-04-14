from flask import Flask, jsonify, render_template
import os
import pandas as pd
from datetime import datetime
import time

from random import *

app=Flask(__name__)
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/pegar', methods=['POST'])
def pegar():
    data = str(randint(1,100))
    
    return data

if __name__ == '__main__':
    app.run(debug=True, port=port)