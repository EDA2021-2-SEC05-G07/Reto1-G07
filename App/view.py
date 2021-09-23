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
        print(artistasCro(catalog))
    elif int(inputs[0]) == 3:
        print(obrasCro(catalog))
        pass

    else:
        sys.exit(0)
sys.exit(0)
