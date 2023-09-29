# Generador de Credenciales

Generador de credenciales para eventos

## Instrucción

Clonar este repositorio:

```shell
gh repo clone pythoncanarias/credenciales
```

Instalar las dependencias (Seguramente mejor en un entorno virtual):

```py
pip install -r requirements.txt
```

## Software adicional

Además de esto, tenemos que tener instalado y accesible desde el _path_ el
programa [Inkscape](https://inkscape.org/es/), para convertir de .SVG a PDF, y
la utilidad [Pdf-tk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/)
para incluir una serie de paginas PDF en un solo documento final.

Para ver si estos programas estan instalados:

```
$ inkscape -V
```

Que debería devolver algo parecido a:

```
Inkscape 1.2.2 (1:1.2.2+202305151914+b0a8486541)
```

y luego:

```shell
$ pdftk --version
```

Que debería devolver algo parecido a:

```
pdftk port to java 3.2.2 a Handy Tool for Manipulating PDF Documents
Copyright (c) 2017-2018 Marc Vinyals - https://gitlab.com/pdftk-java/pdftk
Copyright (c) 2003-2013 Steward and Lee, LLC.
pdftk includes a modified version of the iText library.
Copyright (c) 1999-2009 Bruno Lowagie, Paulo Soares, et al.
This is free software; see the source code for copying conditions. There is
NO warranty, not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

## Ejecución del programa

```shell
$ python generar_credenciales.py ejemplo-plantilla.svg ejemplo-datos.csv
```

Cambiando los ficheros de plantilla y datos para ajustarse a tu caso.

