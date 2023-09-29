all: clean-output
    python generar_credenciales.py credenciales-A6.svg Attendees.csv
    pdftk /home/jileon/temp/pages/*.pdf cat output ./credenciales-A6-pycones2023.pdf

clean-output:
    rm -f /home/jileon/temp/pages/qr*.png
    rm -f /home/jileon/temp/pages/*.svg
    rm -f /home/jileon/temp/pages/*.pdf

clean-input:
    python cleaner.py


asistentes:
    python generar_credenciales.py credenciales-A6.svg participantes.csv


