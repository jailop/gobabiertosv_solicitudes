#!/usr/bin/python

import pandas as pd

INPUT_FILE = 'input/solicitudes-draft.csv'
OUTPUT_FILE = 'input/solicitudes.csv'

def clean(data):
    res = data[~data['Año de admisión'].isnull()].fillna('NA').copy()
    res['Año de admisión'] = res['Año de admisión'].map(lambda x: int(x))
    res.loc[(res['Nivel educativo'] == 'No especificó su inf. académica'), 'Nivel educativo'] = 'NA'
    res.loc[(res['Nivel educativo'] == 'no especificó'), 'Nivel educativo'] = 'NA'
    res.loc[(res['Nivel educativo'] == 'Sin educación formal'), 'Nivel educativo'] = '0 - Sin educación formal'
    res.loc[(res['Nivel educativo'] == 'Primaria (Hasta sexto grado)'), 'Nivel educativo'] = '1 - Primaria'
    res.loc[(res['Nivel educativo'] == 'primaria'), 'Nivel educativo'] = '1 - Primaria'
    res.loc[(res['Nivel educativo'] == 'Secundaria (Tercer ciclo)'), 'Nivel educativo'] = '2 - Secundaria'
    res.loc[(res['Nivel educativo'] == 'secundaria'), 'Nivel educativo'] = '2 - Secundaria'
    res.loc[(res['Nivel educativo'] == 'bachillerato'), 'Nivel educativo'] = '3 - Bachillerato'
    res.loc[(res['Nivel educativo'] == 'Bachillerato'), 'Nivel educativo'] = '3 - Bachillerato'
    res.loc[(res['Nivel educativo'] == 'Universitario'), 'Nivel educativo'] = '4 - Universitario'
    res.loc[(res['Nivel educativo'] == 'universitario'), 'Nivel educativo'] = '4 - Universitario'
    res.loc[(res['Nivel educativo'] == 'Postgrado'), 'Nivel educativo'] = '5 - Posgrado'
    res.loc[(res['Nivel educativo'] == 'postgrado'), 'Nivel educativo'] = '5 - Posgrado'
    res['Nivel educativo'] = res['Nivel educativo'].fillna('NA')
    return res

if __name__ == '__main__':
    data = pd.read_csv(INPUT_FILE)
    data = clean(data)
    data.to_csv(OUTPUT_FILE, index=False)
