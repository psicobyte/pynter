# pynter


Pequeño módulo que genera una imagen basándose en una cadena conteniendo una sucesión arbitraria de 25 unos y ceros. Cada cadena concreta tiene su propia imagen única.

Dependdeindo de la paridad de la cadena, genera un cuadro al estilo de Mondrian o un "mandala" de iconos predefinidos.

## Requisitos:

Este módulo usa mandalillo25 y PiMondrian (incluídos en este repositorio).

mandalillo25 usa los siguientes módulos:

* copy
* math
* re
* sys
* PIL

PiMondrian usa los siguientes módulos:

* hashlib
* PIL
* ImageDraw


## Uso:

Este módulo sólo tiene una función, la función `pinta_cuadro`, que admite una cadena (que debería ser de 25 unos y ceros) y retorna un objeto `Image` de `PIL`

pynter.py está ideado para ser usado como módulo en otros programas de este modo:

    import pynter

    cadena = "0000100110011101011101000"

    salida = pynter.pinta_cuadro(cadena)

    salida.save("cuadro.png")


## Archivos en este repo:

archivo | Descripción
-------|--------
pynter.py | El módulo en sí.
mandalillo.py | El módulo que dibuja los "mandalas".
PiMondrian.py | El módulo que dibuja los "Mondrians".
ejemplo_random.py | Script de ejemplo que usa el módulo pynter.pl para generar una imagen aleatoria.
img | Directorio conteniendo los iconos, colores, etc que se usan para componer los "mandalas".
LICENSE | Licencia (GPL3).
README.MD | Este documento.
