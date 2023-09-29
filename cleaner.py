#!/usr/bin/env python3

import argparse

from rich.markdown import Markdown
from rich.console import Console
import pandas as pd

from transformers import (
    get_codigo_menu,
    get_empresa,
    get_fixed,
    get_pronombre,
    get_talla_camisa,
    )


def load_and_clean(filename):
    people = pd.read_csv(filename)
    people.fillna('', inplace=True)
    names_map = {
        'N.º de pedido': 'id_pedido',
        'Asistente n.º': 'id_asistente',
        'nombre': 'nombre',
        'primer_apellido': 'primer_apellido',
        'segundo_apellido': 'segundo_apellido',
        # 'Apellidos': 'apellidos',
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
    cleaned['nombre'] = cleaned['nombre'].map(get_fixed)
    cleaned['primer_apellido'] = cleaned['primer_apellido'].map(get_fixed)
    cleaned['segundo_apellido'] = cleaned['segundo_apellido'].map(get_fixed)
    return cleaned


def get_arguments():
    parser = argparse.ArgumentParser(
        prog='Limpia los datos de entrada',
        description=(
            'Limpia, fija y da esplendor'
            ' a los ficheros de entrada.'
            ),
        )
    parser.add_argument('input_filename', help="Fichero de entrada")
    parser.add_argument('output_filename', help="Fichero de salida")
    parser.add_argument(
        '-p', '--placeholder',
        default='Asistente',
        action='store',
        )    
    return parser.parse_args()


def main():
    console = Console()
    options = get_arguments()
    cleaned = load_and_clean(options.input_filename)
    cleaned['placeholder'] = options.placeholder
    console.print(Markdown(
        f'Generando el fichero de **{options.placeholder}**'
        f' a partir de `{options.input_filename}`'
        f' La salida estará en `{options.output_filename}`.'
        ))
    cleaned.to_csv(options.output_filename, index=False)


if __name__ == "__main__":
    main()
