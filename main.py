#!/usr/bin/python

import pandas as pd
import getdata
import clean
import process

if __name__ == '__main__':
    # Getting data
    data = getdata.download_file()
    getdata.save_file(data)
    # Cleaning data
    INPUT_FILE = 'input/solicitudes-draft.csv'
    OUTPUT_FILE = 'input/solicitudes.csv'
    data = pd.read_csv(INPUT_FILE)
    data = clean.clean(data)
    data.to_csv(OUTPUT_FILE, index=False)
    # Processing data
    data = pd.read_csv('input/solicitudes.csv')
    process.by_sex(data)
    process.by_place(data)
    process.by_education_level(data)
    process.by_age(data)
