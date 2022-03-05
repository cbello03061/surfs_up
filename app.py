
from flask import Flask
from sqlalchemy import true
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')

def home():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=true)

    
