#!/usr/bin/python
#coding: utf-8

#       CopyRight 2016 Allan Psicobyte (psicobyte@gmail.com)
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.


import mandalillo
import PiMondrian
import re

def pinta_cuadro(cadena_de_bits):

    if re.match('^[0-1]*$', cadena_de_bits) and len(cadena_de_bits) == 25:

        paridad = sum(int(i) for i in cadena_de_bits)%2

        if paridad == 0:
            salida = PiMondrian.mondrian(cadena_de_bits)

        else:
            imagen = mandalillo.Mandalillo(cadena_de_bits)
            salida = imagen.dibuja()
        return salida
    else:
        raise ValueError('se esperaban 25 digitos binarios')


if __name__ == "__main__":


print """
pynter.py genera una imagen basándose en una cadena conteniendo una sucesión arbitraria de 25 unos y ceros. Cada cadena concreta tiene su propia imagen única.

pynter.py está ideado para ser usado como módulo en otros programas de este modo:

    import pynter

    cadena = "0000100110011101011101000"

    salida = pynter.pinta_cuadro(cadena)

    salida.save("cuadro.png")
"""
