set dotenv-load

export output_dir := env_var_or_default('OUTPUT_DIR', 'output')

sample: clean_output
    python generar_credenciales.py ejemplo-plantilla.svg ejemplo-datos.csv --debug
    pdftk {{ output_dir }}/*.pdf cat output ./ejemplo.pdf


clean_output:
    rm -f /home/jileon/temp/pages/qr*.png
    rm -f /home/jileon/temp/pages/*.svg
    rm -f /home/jileon/temp/pages/*.pdf

clean_input:
    python cleaner.py organizacion-raw.csv organizacion.csv -p "Organización"
    python cleaner.py voluntariado-raw.csv voluntariado.csv -p "Voluntariado"
    python cleaner.py ponentes-raw.csv ponentes.csv -p "Ponente"
    python cleaner.py keynoters-raw.csv keynoters.csv -p "Keynoter"
    python cleaner.py patrocinadores-raw.csv patrocinadores.csv -p "Patrocinio"
    python cleaner.py colaboradores-raw.csv colaboradores.csv -p "Colaboración"
    python cleaner.py asistentes-raw.csv asistentes.csv -p "Asistente"


clean_all: clean_output clean_input

all: organizacion voluntariado

organizacion: clean_output
    python generar_credenciales.py ejemplo-plantilla.svg organizacion.csv
    pdftk {{ output_dir }}/*.pdf cat output ./credenciales-A6-organizacion-pycones2023.pdf

voluntariado: clean_output
    python generar_credenciales.py ejemplo-plantilla.svg voluntariado.csv
    pdftk {{ output_dir }}/*.pdf cat output ./credenciales-A6-voluntariado-pycones2023.pdf

ponentes: clean_output
    python generar_credenciales.py ejemplo-plantilla.svg ponentes.csv
    pdftk {{ output_dir }}/*.pdf cat output ./credenciales-A6-ponentes-pycones2023.pdf

keynoters: clean_output
    python generar_credenciales.py ejemplo-plantilla.svg keynoters.csv
    pdftk {{ output_dir }}/*.pdf cat output ./credenciales-A6-keynoters-pycones2023.pdf

patrocinadores: clean_output
    python generar_credenciales.py ejemplo-plantilla.svg patrocinadores.csv
    pdftk {{ output_dir }}/*.pdf cat output ./credenciales-A6-patrocinadores-pycones2023.pdf

colaboradores: clean_output
    python generar_credenciales.py ejemplo-plantilla.svg colaboradores.csv
    pdftk {{ output_dir }}/*.pdf cat output ./credenciales-A6-colaboradores-pycones2023.pdf

asistentes: clean_output
    python generar_credenciales.py ejemplo-plantilla.svg asistentes.csv
    pdftk {{ output_dir }}/*.pdf cat output ./credenciales-A6-asistentes-pycones2023.pdf
