from emotion1 import emotion
from Age import age
from flask import Flask, request, render_template
import threading
import time
app = Flask(__name__,template_folder='templates')

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/emotion')
def emo():
    emotion()

@app.route('/age')
def ager():
    age()

    
    
if __name__ == '__main__':
    app.run()
    
        
    
    
