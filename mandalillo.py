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

import copy
import math
import re
import sys
from PIL import Image

coordenadas_del_centro = (400,400)

radio_maximo = 375

archivos_iconos = ("img/glifo1.png","img/glifo2.png","img/glifo3.png","img/glifo4.png","img/glifo5.png","img/glifo6.png","img/glifo7.png","img/glifo8.png")

archivos_colores = ("img/color1.png","img/color2.png","img/color3.png","img/color4.png","img/color5.png","img/color6.png","img/color7.png","img/color8.png")

archivos_fondos = ("img/fondo1.png","img/fondo2.png","img/fondo3.png","img/fondo4.png","img/fondo5.png","img/fondo6.png","img/fondo7.png","img/fondo8.png")


class Mandalillo:
    def __init__(self,cadena):

        if re.match('^[0-1]*$', cadena) and len(cadena) == 25:
            self.primus = Anillo(cadena[0:12],radio_maximo)
            self.secundus = Anillo(cadena[12:24],self.primus.radio_minimo)
            self.tertius = Anillo(cadena[13:25],self.secundus.radio_minimo)

            self.central = int(cadena[10:13],2)
            self.color_central = int(cadena[7:10],2)
            imagen_fondo = int(cadena[4:7],2)

            self.sello = Representacion(imagen_fondo)
        else:
            raise ValueError('se esperaban 25 digitos binarios')

    def dibuja(self):
        fondo = self.primus.dibuja(0, self.sello, coordenadas_del_centro)
        fondo = self.secundus.dibuja(0, self.sello, coordenadas_del_centro)
        fondo = self.tertius.dibuja(0, self.sello, coordenadas_del_centro)

        fondo = self.sello.ubicar(self.central,coordenadas_del_centro,270,(2*self.tertius.radio_minimo,2*self.tertius.radio_minimo),self.color_central)

        return fondo



class Anillo:

    def __init__(self,cadena,radio_maximo):
        self.icono = int(cadena[0:3],2)
        self.color_par = int(cadena[3:6],2)
        self.color_impar = int(cadena[6:9],2)
        self.numero = (int(cadena[9:12],2) + 2 ) * 2

        self.radio_centros = radio_maximo / (math.sin(math.radians(180 / self.numero)) + 1)
        self.tamano_icono = 2 * self.radio_centros * math.sin(math.radians(180 / self.numero))
        self.radio_minimo = radio_maximo - self.tamano_icono


    def dibuja(self,offset,sello,centro):

        for paso in range(0,self.numero):

            angulo = (paso * 360 / self.numero) + offset

            y = self.radio_centros * math.sin(math.radians(angulo)) + centro[1]
            x = self.radio_centros * math.cos(math.radians(angulo)) + centro[0]
            if paso %2 == 0:
                color = self.color_par
            else:
                color = self.color_impar

            fondo = sello.ubicar(self.icono,(x,y),angulo,(self.tamano_icono,self.tamano_icono),color)

        return fondo




class Representacion:
    def __init__(self,numero):


        self.icono = list()
        for i in archivos_iconos:
            self.icono.append(Image.open(i))

        self.color = list()
        for i in archivos_colores:
            self.color.append(Image.open(i))

        self.fondo = Image.open(archivos_fondos[numero])


    def ubicar(self ,img, posicion, angulo, tamano, col):
        imagen = self.icono[img]

        imagen_fondo = copy.copy(self.color[col])

        imagen_fondo.paste(imagen, (0,0), imagen)

        angulo += 90
        imagen_fondo = imagen_fondo.rotate(-angulo)

        ancho = int(tamano[0])
        alto = int(tamano[1])
        imagen_fondo = imagen_fondo.resize((ancho,alto), Image.ANTIALIAS)
        x = int(posicion[0] - (ancho / 2))
        y = int(posicion[1] - (alto / 2))

        self.fondo.paste(imagen_fondo, (x,y), imagen_fondo)
        return self.fondo




if __name__ == "__main__":

    if len(sys.argv) > 1:
        input_string = sys.argv[1]

        imagen = Mandalillo(input_string)
        salida = imagen.dibuja()
        salida.save("salida.png")

    else:
        print "Uso: mandalillo.py <STRING>"
        print "Donde <STRING> deben cuarenta unos y ceros"
        print "Ejemplo: mandalillo.py 0000100110011101011101000010010010110100"
