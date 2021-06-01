import requests
import json
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import configparser

config = configparser.ConfigParser()
config.read('data/config.conf')
api_key = config['API']['API_KEY']


def all_sets():
    result = requests.get("https://api.pokemontcg.io/v2/sets", headers={"X-Api-Key": api_key})
    return result.json()["data"]


def get_img(url):
    img2 = Image.open(requests.get(url, stream=True).raw)
    return img2


def get_set_info(set_id):
    result = requests.get("https://api.pokemontcg.io/v2/sets/" + set_id, headers={"X-Api-Key": api_key})
    return result.json()["data"]


def get_cards_from_set(set_id):
    result = requests.get("https://api.pokemontcg.io/v2/cards?q=set.id:" + set_id, headers={"X-Api-Key": api_key})
    owned_data = []
    try:
        f = open('data/owned.json', 'r')
        owned_data = json.load(f)
        f.close()
    except FileNotFoundError:
        messagebox.showerror('File not found', 'There is no file named owned.json in data directory!')
    result = result.json()["data"]
    for od in range(len(owned_data)):
        for c in range(len(result)):
            if result[c]["id"] == owned_data[od]["id"] and owned_data[od]["owned"]:
                result[c]["owned"] = 1

    for c in range(len(result)):
        if "owned" not in result[c]:
            result[c]["owned"] = 0
    return result


def search_card_by_name(card_name):
    result = requests.get("https://api.pokemontcg.io/v2/cards?q=name:*" + card_name + "*",
                          headers={"X-Api-Key": api_key})
    owned_data = []
    try:
        f = open('data/owned.json', 'r')
        owned_data = json.load(f)
        f.close()
    except FileNotFoundError:
        messagebox.showerror('File not found', 'There is no file named owned.json in data directory!')
    result = result.json()["data"]
    for od in range(len(owned_data)):
        for c in range(len(result)):
            if result[c]["id"] == owned_data[od]["id"] and owned_data[od]["owned"]:
                result[c]["owned"] = 1

    for c in range(len(result)):
        if "owned" not in result[c]:
            result[c]["owned"] = 0
    return result


def get_number_of_owned_cards():
    f = open('data/owned.json', 'r')
    owned_data = json.load(f)
    result = 0
    for c in owned_data:
        result += c["owned"]
    f.close()
    return result


def get_owned_cards():
    f = open('data/owned.json', 'r')
    owned_data = json.load(f)
    f.close()
    s_id = ''
    for c in owned_data:
        if c["owned"]:
            if s_id:
                s_id += ' OR '
            s_id += 'id:' + c["id"]
    result = requests.get("https://api.pokemontcg.io/v2/cards?q=(" + s_id + ")",
                          headers={"X-Api-Key": api_key})
    result = result.json()["data"]
    for od in range(len(owned_data)):
        for c in range(len(result)):
            if result[c]["id"] == owned_data[od]["id"] and owned_data[od]["owned"]:
                result[c]["owned"] = 1

    for c in range(len(result)):
        if "owned" not in result[c]:
            result[c]["owned"] = 0
    return result
