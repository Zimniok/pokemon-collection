import json
import http.client

with open('NeoGenesis.json') as json_file:
    data = json.load(json_file)

def searchByID(id):
    for card in data:
        if card['number'] == str(id):
            return(card)
def getCards():
    return {'data':[{'name':i['name'], 'id':i['number'], 'owned':i['owned']} for i in data]}

def setCard(id, status):
    searchByID(id)['owned'] = status
    save()
    return status

def save():
    with open('NeoGenesis.json', 'w') as json_file:
        json.dump(data, json_file)
