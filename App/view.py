"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from App.controller import getprimeros3
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1 - Cargar información en el catálogo")
    print("2 - Listar cronológicamente los artistas")
    print("3 - Listar cronológicamente las adquisiones")
    print("4 - Clasificar las obras de un artista por técnica")
    print("5 - Clasificar las obras por la nacionalidad de sus creadores")
    print("6 - Transportar obras de un departamento")
    print("7 - Proponer una nueva exposición en el museo")

catalog = None

def initDatos():
    return controller.initDatos()

def cargarDatos(catalog):
    return controller.cargarDatos(catalog)

def artistasCro(catalog):
    return controller.getartistasCro()

def obrasCro(catalog):
    return controller.getobrasCro()

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog= initDatos()
        cargarDatos(catalog)
        print('Numero de artistas: '+ str(lt.size(catalog['Artists'])))
        print('Numero de obras: '+ str(lt.size(catalog['Artworks'])))
        print('Ultimos 3 elementos del archivo artistas: '+ str(lt.subList(catalog['Artists'],lt.size(catalog['Artists'])-2,3)))
        print('Ultimos 3 elementos del archivo obras: '+ str(lt.subList(catalog['Artworks'],lt.size(catalog['Artworks'])-2,3)))

    elif int(inputs[0]) == 2:
        inicial= input('Ingrese la fecha inicial del rango: ')
        final= input('Ingrese la fecha final del rango: ')
        artistas=controller.getorgartistascro(catalog,inicial,final)
        print('Número total de artistas en el rango: ') + str(artistas[1])
        ordenada= controller.getordenarArtistas(artistas)
        print('Primeros 3 artistas del rango cronologico: ') + str(controller.getprimeros3(ordenada))
        print('Ultimos 3 artistas del rango cronológico: ')+ str(controller.getultimos3(ordenada))

    elif int(inputs[0]) == 3:
        inicial= input('Ingrese la fecha inicial del rango: ')
        final= input('Ingrese la fecha final del rango: ')
        print('Número total de obras en el rango cronológico: ')
        print('Número total de obras adquiridas por compra (“purchase…”)')
        print('Primeras 3 obras del rango')
        print('últimas 3 obras del rango)
    elif int(inputs[0]) == 4:
        nombre=input('Ingrese el nombre de un artista: ')
        print('Total de obras')
        print('Total técnicas utilizadas')
        print('La técnica mas utilizada')
        print('El listado de las obras de dicha técnica')
    elif int(inputs[0]) == 5:
        print('Lista de nacionalidades ordenadas por el total de obras de mayor a menor (TOP 10).')
        print('Información de las obras de la nacionalidad con el mayor numero de obras')

    elif int(inputs[0]) == 6:
        print('Total de obras para transportar')
        print('Estimado en USD del precio del servicio')
        print('Peso estimado de las obras')
        print('Las 5 obras mas antiguas a transportar')
        print('Las 5 obras mas costosas para transportar')
    
        pass

    else:
        sys.exit(0)
sys.exit(0)
