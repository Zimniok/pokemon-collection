
from flask import Flask
from flask_cors import CORS
import p
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/card/id/<id>')
def getCardByID(id=None):
    return p.searchByID(id)

@app.route('/card/set/<id>/<status>')
def setCard(id=None,status=None):
    return p.setCard(id,status)

@app.route('/all_cards')
def getAllCards():
    return p.getCards()

if __name__ == '__main__':
    app.run(debug=True)
