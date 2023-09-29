#!/usr/bin/env python3

import pandas as pd

from transformers import (
    get_codigo_menu,
    get_empresa,
    get_nombre,
    get_primer_apellido,
    get_pronombre,
    get_segundo_apellido,
    get_talla_camisa,
    )


def load_and_clean(filename):
    people = pd.read_csv(filename)
    names_map = {
        'N.º de pedido': 'id_pedido',
        'Asistente n.º': 'id_asistente',
        'Nombre': 'nombre',
        'Apellidos': 'apellidos',
        # 'Correo electrónico': 'email',
        'Elige tu talla de camiseta': 'camisa',
        'Elige tu menú': 'menu',
        # '¿Alguna alergia alimenticia?': 'alergias',
        '¿Cuáles son tus pronombres?': 'pronombre',
        'Introduce el nombre de tu empresa o entidad': 'empresa',
        }
    cleaned = people[names_map.keys()].rename(columns=names_map)
    cleaned['camisa'] = cleaned['camisa'].map(get_talla_camisa)
    cleaned['menu'] = cleaned['menu'].map(get_codigo_menu)
    cleaned['pronombre'] = cleaned['pronombre'].map(get_pronombre)
    cleaned['empresa'] = cleaned['empresa'].map(get_empresa)
    cleaned['nombre'] = cleaned['nombre'].map(get_nombre)
    cleaned['primer_apellido'] = cleaned['apellidos'].map(get_primer_apellido)
    cleaned['segundo_apellido'] = cleaned['apellidos'].map(get_segundo_apellido)
    return cleaned


def main():
    cleaned = load_and_clean('Attendees.csv')
    cleaned['placeholder'] = 'Asistente'
    cleaned.to_csv('participantes.csv', index=False)


if __name__ == "__main__":
    main()
