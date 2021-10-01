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
        inicial= input('Ingrese la fecha inicial del rango: ')
        final= input('Ingrese la fecha final del rango: ')
        artistas=controller.getorgartistascro(catalog,inicial,final)
        print('Número total de artistas en el rango: ' + str(artistas[1]))
        ordenada= controller.getordenarArtistas(artistas)
        print('Primeros 3 artistas del rango cronologico: ' + str(controller.getprimeros3(ordenada)))
        print('Ultimos 3 artistas del rango cronológico: '+ str(controller.getultimos3(ordenada)))

    elif int(inputs[0]) == 3:
        inicial= input('Ingrese la fecha inicial del rango: ')
        final= input('Ingrese la fecha final del rango: ')
        obras = controller.getorgObrasCro(catalog, inicial, final)
        print('Número total de obras en el rango cronológico: '+ str(obras[1]))
        obras_purchase = controller.getnumPurchase(catalog)
        print('Número total de obras adquiridas por compra "purchase"' +str(obras_purchase))
        ordenada= controller.getordenarObras(obras[0])
        print('Primeras 3 obras del rango' + str(controller.getprimeros3(ordenada)))
        print('últimas 3 obras del rango' + str(controller.getultimos3(ordenada)))

    elif int(inputs[0]) == 4:
        nombre=input('Ingrese el nombre de un artista: ')
        encontrarid = controller.getenconID(catalog, nombre)
        obras= controller.gettecnicasartista(catalog, encontrarid)
        print('Total de obras: '+ str(obras[0]))
        tecnicas= controller.getcantidadtecnicas(tecnicas)
        print('Total técnicas utilizadas: ' +str(tecnicas))
        tecni_mas_usada= controller.gettecnimasusada(tecnicas)
        print('La técnica mas utilizada es: ' +str(tecni_mas_usada))
        lista = controller.getlistaObras(catalog, tecni_mas_usada, tecnicas)
        print('El listado de las obras de dicha técnica: ') + lista

    elif int(inputs[0]) == 5:
        nacioNombre = controller.getidyNacio(catalog, id)
        lista = controller.getlista_nacionalidades(nacioNombre)
        print('Lista de nacionalidades ordenadas por el total de obras de mayor a menor (TOP 10).' + str(lista))
        top10= controller.getTop10(nacioNombre)
        info_obras= controller.getnacioMasObras(top10, catalog)
        print('Información de las obras de la nacionalidad con el mayor numero de obras') + info_obras

    elif int(inputs[0]) == 6:
        departamento = input('Departamento del museo: ')
        lista = controller.getobrasDepartamento(departamento, catalog)
        total_obras= controller.getcantidadObras(lista)
        print('Total de obras para transportar: ' + str(total_obras))
        costoObras = controller.getdictCostos(lista)
        estimado = controller.getcostoEstimado(costoObras)
        print('Estimado en USD del precio del servicio: ' + str(estimado))
        peso_estimado = controller.getpesototal(lista)
        print('Peso estimado de las obras: ' + str(peso_estimado))
        listafechas= controller.getlistafechas(lista)
        listaOrdenada= controller.getordenarlista(listafechas)
        obras_antiguas = controller.getobrasMasAntiguas(listaOrdenada, catalog, lista)
        print('Las 5 obras mas antiguas a transportar: ' + obras_antiguas)
        listaprecios = controller.getlistaprecios(costoObras)
        listaOrdenadaprecios = controller.getordenarlista2(listaprecios)
        obras_costosas = controller.getobrasMasCost(listaOrdenadaprecios, catalog, lista)
        print('Las 5 obras mas costosas para transportar: ' + obras_costosas)
    
    else:
        sys.exit(0)
sys.exit(0)
