#!/usr/bin/python

import requests
import pandas as pd

URL_FILE = 'conf/dataset-url.txt'
DATA_FILE = 'input/solicitudes-draft.csv'

def download_file():
    """
    It downloads the dataset from Portal de Datos Abiertos.
    The dataset link is stored in URL_FILE.
    A unique string containing the data is returned.
    """
    fin = open(URL_FILE, 'r')
    url = fin.read()
    fin.close()
    req = requests.get(url)
    raw = str(req.content.decode('iso-8859-1'))
    return raw

def save_file(data):
    """
    It does just that. It saves data to the
    dataset output file.
    """
    fout = open(DATA_FILE, 'w')
    fout.write(data)
    fout.close()

if __name__ == '__main__':
    data = download_file()
    save_file(data)
