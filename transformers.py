#!/usr/bin/env python3

import random
import numpy as np


def anonimize(s):
    letras = list(s)
    random.shuffle(letras)
    result = ''.join(letras)
    if ' ' in result:
        return ' '.join([
            _.capitalize()
            for _ in result.split()
        ])
    return result


def get_codigo_menu(menu):

    # OMNI = '1'
    # VEG = '2'
    # CELIACO = '3'

    OMNI = '✱'
    VEG = '▼'
    CELIACO = '©'

    return {
        'Sin restricciones.': OMNI,
        'Vegetariano': VEG,
        'Sin restricciones. | Celiaco': CELIACO,
        'Vegano': VEG,
        'Celiaco': CELIACO,
        'Vegano. | Vegetariano': VEG,
        'Sin restricciones. | Vegetariano': VEG,
        'Vegano. | Especial Celiaco | Vegetariano': CELIACO,
        'Vegano | Vegetariano': VEG,
    }.get(menu)


def get_pronombre(pronombre):
    return {
        'él': 'él',
        'ella': 'ella',
        'elle': 'elle',
    }.get(pronombre, '')


def get_talla_camisa(camisa):
    CODIGO_SIN_CAMISA = '0'
    CODIGO_XS = '1'
    CODIGO_S = '2'
    CODIGO_M = '3'
    CODIGO_L = '4'
    CODIGO_XL = '5'
    CODIGO_XXL = '6'
    CODIGO_3XL = '7'
    return {
        'No quiero camiseta, prefiero el regalo alternativo.': CODIGO_SIN_CAMISA,
        'XS': CODIGO_XS,
        'S': CODIGO_S,
        'M': CODIGO_M,
        'L': CODIGO_L,
        'XL': CODIGO_XL,
        'XXL': CODIGO_XXL,
        '3XL': CODIGO_3XL,
    }.get(camisa)


def get_empresa(empresa):
    if empresa is np.nan:
        return ''
    if empresa:
        return str(empresa).strip()
    return ''


FIXES = {
    'Aaron': 'Aarón',
    'Abadia': 'Abadía',
    'Alvaro': 'Álvaro',
    'Calderon': 'Calderón',
    'Dominguez': 'Domínguez',
    'Fernandez': 'Fernández',
    'Hernandez': 'Hernández',
    'Garcia': 'García',
    'Gomez': 'Gómez',
    'Gonzalez': 'González',
    'Jimenez': 'Jiménez',
    'Jose': 'José',
    'Lopez': 'López',
    'Maria': 'María',
    'Martin': 'Martín',
    'Martinez': 'Martínez',
    'Jesus': 'Jesús',
    'Perez': 'Pérez',
    'Ramon': 'Ramón',
    'Rodriguez': 'Rodríguez',
    'Roman': 'Román',
    'Ruben': 'Rubén',
    'Sanchez': 'Sánchez',
    'Simon': 'Simón',
    'Suarez': 'Suárez',
    'Vazquez': 'Vázquez',
    'Verdu': 'Verdú',
}

def get_nombre(nombre):
    nombre = nombre.strip()
    words = [fix(_) for _ in nombre.split()]
    return ' '.join(words)


def fix(texto):
    texto = texto.replace('a\u0301', 'á')
    texto = texto.replace('A\u0301', 'Á')
    texto = texto.replace('e\u0301', 'é')
    texto = texto.replace('E\u0301', 'É')
    texto = texto.replace('i\u0301', 'í')
    texto = texto.replace('I\u0301', 'Í')
    texto = texto.replace('o\u0301', 'ó')
    texto = texto.replace('O\u0301', 'Ó')
    texto = texto.replace('u\u0301', 'ú')
    texto = texto.replace('U\u0301', 'Ú')
    texto = texto.strip().capitalize()
    return FIXES.get(texto, texto)

    
def split_apellidos(apellidos):
    apellidos = apellidos.strip()
    if ' ' not in apellidos:
        return (fix(apellidos), '')
    space_in = apellidos.index(' ')
    if space_in < 4:
        primer_apellido, segundo_apellido = apellidos.rsplit(maxsplit=1)
    else:
        primer_apellido, segundo_apellido = apellidos.split(maxsplit=1)
    return fix(primer_apellido), fix(segundo_apellido)


def get_primer_apellido(s):
    return split_apellidos(s)[0]


def get_segundo_apellido(s):
    return split_apellidos(s)[1]
