#!/usr/bin/python

import numpy as np
import pandas as pd

def by_sex(data):
    res = pd.crosstab(data['Año de admisión'], data['Sexo'])
    res.to_excel('xlsx/por-sexo.xlsx', sheet_name='Por sexo')
    res.to_csv('csv/por-sexo.csv')
    res = res / 1000
    fig = res.plot(kind='bar', alpha=0.5, title='Solicitudes por sexo')
    fig.set_ylabel('Miles de solicitudes')
    fig.get_figure().savefig('chart/por-sexo.png', dpi=150, bbox_inches="tight", transparent=True)
    return res

def by_place(data):
    res = pd.crosstab([data['Departamento'], data['Municipio']], data['Año de admisión'])
    res.to_excel('xlsx/por-lugar.xlsx', sheet_name='Por lugar')
    res.to_csv('csv/por-lugar.csv')
    return res

def by_education_level(data):
    res = pd.crosstab(data['Nivel educativo'], data['Año de admisión'])
    res.to_excel('xlsx/por-nivel-educativo.xlsx', sheet_name='Por nivel educativo')
    res.to_csv('csv/por-nivel-educativo.csv')
    res = res / 1000
    fig = res.plot(kind='bar', alpha=0.5, title='Solicitudes por nivel educativo')
    fig.set_ylabel('Miles de solicitudes')
    fig.get_figure().savefig(
        'chart/por-nivel-educativo.png', 
        dpi=150, 
        bbox_inches="tight", 
        transparent=True
    )
    return res

def by_age(data):
    tmp = data.groupby(['Edad'])['Edad'].count()
    edades = [0, 18, 30, 45, 60,100]
    freq = np.zeros(len(edades) - 1)
    pos = 1
    for idx in range(len(tmp)):
        if pos > len(edades) - 2:
            break
        if idx >= edades[pos]:
            pos += 1
        freq[pos - 1] += tmp.iloc[idx]
    res = pd.DataFrame(
        {'Frecuencia': freq}, 
        index=['[0-18]', '(18-30]', '(30-45]', '(45-60]', '>60']
    )
    res.to_excel('xlsx/por-rango-edad.xlsx', sheet_name='Por rangos de edad')
    res.to_csv('csv/por-rango-edad.csv')
    res = res / 1000
    fig = res.plot(kind='bar', alpha=0.5, title='Solicitudes por rango de edad')
    fig.set_ylabel('Miles de solicitudes')
    fig.get_figure().savefig(
        'chart/por-rango-edad.png', 
        dpi=150, 
        bbox_inches="tight", 
        transparent=True
    )
    return res

def by_unit(data):
    res = pd.crosstab(data['Institución'], data['Año de admisión'])
    res = res.sort_values(by=[2017, 2016, 2015, 2014], ascending=False)
    res.to_excel('xlsx/por-institucion.xlsx', sheet_name='Por institucion')
    res.to_csv('csv/por-institucion.csv')
    return res

if __name__ == '__main__':
    data = pd.read_csv('input/solicitudes.csv')
    by_sex(data)
    by_place(data)
    by_education_level(data)
    by_age(data)
    by_unit(data)

