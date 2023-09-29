#!/usr/bin/env python3

from pathlib import Path
import argparse
import os
import subprocess

import pandas as pd
from jinja2 import Environment, FileSystemLoader
from tqdm import tqdm
from prettyconf import config


def get_arguments():
    output_dir = config('OUTPUT_DIR', cast=Path, defaul=Path('./pages'))
    debug = config('DEBUG', cast=config.boolean, default=False)
    parser = argparse.ArgumentParser(
        prog='Generador de credenciales',
        description='Genera, esto... credenciales',
        )
    parser.add_argument('template_filename', help="Platilla a usar")
    parser.add_argument('input_filename', help="Fichero CSV con los datos")
    parser.add_argument(
        '-p', '--placeholder',
        default='Asistente',
        action='store',
        )
    parser.add_argument(
        '-o', '--output-dir',
        default=output_dir,
        action='store',
        )
    parser.add_argument(
        '-d', '--debug',
        default=debug,
        action='store_true',
        )
    result = parser.parse_args()
    os.makedirs(result.output_dir, exist_ok=True)
    return result


def load_template(template_filename):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_filename)
    return template


def make_batch(template, input_file, **kwargs):
    output_dir = kwargs.get('output_dir', './pages')
    debug = kwargs.get('debug', False)
    template = load_template(template)
    cleaned = pd.read_csv(input_file)
    print(f'Voy que preparar {cleaned.shape[0]} credenciales')
    if debug:
        cleaned = cleaned.sample(32)
    cleaned = cleaned.sort_values(by=['primer_apellido', 'segundo_apellido'])
    data = [dict(item) for index, item in cleaned.iterrows()]
    print(f'Generando {len(data)} credenciales', end=": ", flush=True)
    for seq, sample in enumerate(tqdm(data), start=1):
        id_asistente = sample['id_asistente']
        sample['warning'] = bool(sample['menu'] != '✱')
        svg_filename = output_dir / f'{seq:04}-{id_asistente}.svg'
        pdf_filename = output_dir / f'{seq:04}-{id_asistente}.pdf'
        with open(svg_filename, 'w', encoding='utf-8') as f:
            f.write(template.render(**sample))
        subprocess.run(
            [
                'inkscape',
                svg_filename,
                '--export-text-to-path',
                '--export-area-page',
                '--export-filename',
                pdf_filename,
            ],
            stderr=subprocess.DEVNULL,
            )
    print("[OK]")


def main():
    args = get_arguments()
    print(
        f'Generando credenciales a partir de la plantilla'
        f' {args.template_filename} con datos de'
        f' {args.input_filename}. Los resultdos temporales'
        f' se almacenaran en {args.output_dir}.'
        )
    make_batch(
        args.template_filename,
        args.input_filename,
        debug=args.debug,
        output_dir=args.output_dir,
        )


if __name__ == "__main__":
    main()
