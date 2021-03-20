from flask import Flask
import p
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/card/id/<id>')
def getCardByID(id=None):
    return p.searchByID(id)

@app.route('/all_cards')
def getAllCards():
    return p.getCards()

if __name__ == '__main__':
    app.run(debug=True)