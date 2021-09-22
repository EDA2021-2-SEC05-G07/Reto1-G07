"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def iniciarDatos():
    catalog={'Artists': None, 'Artworks': None}

    catalog['Artists']= lt.newList()
    catalog['Artworks']= lt.newList()

    return catalog

def addArtist(catalog, artist):
    lt.addLast(catalog['Artists'], artist)

def addArtwork(catalog, artwork):
    lt.addLast(catalog['Artworks'],artwork)


# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def orgartistasCro(catalog, artist):
    datelist=lt.newlist()
    namelist=lt.newlist()
    for artista in lt.iterator(catalog['Artists']):
        fecha=artist['Begin Date']
        lt.addLast(datelist,fecha)
    ordenado= mg.sort(datelist)
    for fecha in lt.iterator(ordenado):
        if fecha == catalog['Artists']['Begin Date']:
            lt.addLast(namelist, catalog['Artist']['Display Name'])
    
    return namelist

def orgobrasCro(catalog, artwork):
    datelist=lt.newlist()
    artworklist=lt.newlist()
    for artista in lt.iterator(catalog['Artworks']):
        fecha=artwork['Date']
        lt.addLast(datelist,fecha)
    ordenado= mg.sort(datelist)
    for fecha in lt.iterator(ordenado):
        if fecha == catalog['Artworks']['Date']:
            lt.addLast(artworklist, catalog['Artworks']['Title'])
    
    return artworklist

def enconID(catalog, nombre):
    i=0
    f=len(catalog['Artists']-1)
    pos=-1
    id= False
    while i <= f and id == False:
        m=(i+f)//2
        if catalog['Artists'][m]== nombre:
            pos=m
            id=True
        elif catalog['Artists'][m] > nombre:
            f=m-1
        else:
            i=m+1
    encontrarid= catalog['Artist'][pos]['Constituent ID']
    return encontrarid
    
def tecnicasartista(catalog, encontrarid):
    cantidadobras=0
    tecnicas={}
    for obra in lt.iterator(catalog['Artworks']):
        if obra['Constituent ID'] == encontrarid:
            cantidadobras+=1
            tecnica= obra['Medium']
            if tecnica in tecnicas:
                lt.addLast(tecnicas[tecnica],obra['Title'])
            else:
                tecnicas[tecnica]=lt.newList()
                lt.addLast(tecnicas[tecnica],obra['Title'])
    return (cantidadobras, tecnicas)

def cantidadtecnicas(tecnicas):
    totalTecni= lt.size(tecnicas)
    return totalTecni

def tecnimasusada(tecnicas:dict):
    mayor=0
    for categoria in tecnicas:
        size= lt.size(categoria)
        if size > mayor:
            mayor= size
            for key in tecnicas.keys():
                if key == tecnicas['categoria']:
                    masusada = key
    return masusada

def listaObras(catalog, masusada, tecnicas):
    for obra in lt.iterator(catalog['Artworks']):
        if obra['Title'] in tecnicas[masusada]:
            x=[obra['Title'], obra['Date'], obra['Medium'], obra['Dimensions']]
            obras=lt.newList()
            lt.addLast(obras,x)
    return obras

def obrasnacionalidad(catalog, encontrarid):
    lst_obras_na = {}
    #toca pasar ese diccionario a lista pq afecta las lineas 150, 154 de model.
    for obra in lt.iterator(catalog['Artworks']):
        if obra['Constituent ID'] == encontrarid:
            nacionalidad = obra['Nationality']
            if nacionalidad in lst_obras_na:
                lst_obras_na[nacionalidad] = obra['Title']
                #lt.addLast(lst_obras_na[nacionalidad], obra['Title'])
                #creo que el addLast no sirve porque lst_obras_na es un diccionario vacio
            else:
                lst_obras_na[nacionalidad]=lt.newList()
                lt.addLast(lst_obras_na[nacionalidad], obra['Title'])
    return (lst_obras_na)

def lista_nacionalidades(lst_obras_na):
    mayor=0
    top10= 0
    lst_nacio_ord = lt.newList
    for obra in lst_obras_na:
        size= lt.size(obra)
        if size > mayor:
            mayor= size
            while top10 <= 10:
                key = lst_obras_na.keys()
                if key == lst_obras_na['Nationality']:
                    nacionalidad_mas_repetida = key
                    top10+= 1
                    lst_top10_final = lt.addLast(lst_nacio_ord,nacionalidad_mas_repetida)
    return lst_top10_final

def nacio_mayor_obras(catalog, lst_top10_final, lst_obras_na):
    for obra in lt.iterator(catalog['Artworks']):
        if obra['Title'] in lst_obras_na[lst_top10_final]:
            #no estoy segura si quedo bien por lo que ambas son listas
            x=[obra['Title'], obra['Date'], obra['Medium'], obra['Dimensions'],  obra['Consituent ID']]
            obras_na= lt.newList
            lt.addLast(obras_na,x)
    return obras_na

def obrasDepartamento(departamento, catalog):
    lista= lt.newList()
    for obra in lt.iterator(catalog['Artworks']):
        if catalog['Artworks']['Department'] == departamento:
            lt.addLast(lista, obra)
    return lista
def ordenar(o1,o2):
    return o1['Date']<o2['Date']

lista=sa.sort(lista, ordenar)

def transportarObras(lista):
    totalObras= lt.size(lista)
