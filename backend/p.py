import json
import http.client

with open('NeoGenesis.json') as json_file:
    data = json.load(json_file)['data']

def searchByID(id):
    for card in data:
        if card['number'] == str(id):
            return(card)
def getCards():
    return {'data':[{'name':i['name'], 'id':i['number']} for i in data]}
