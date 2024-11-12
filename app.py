from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html', result=None) # at loading result will be nothing

from controller import *
