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
    for artista in catalog['Artists']:
        fecha=artist['Begin Date']
        lt.addLast(datelist,fecha)
    ordenado= mg.sort(datelist)
    for fecha in ordenado:
        if fecha == catalog['Artists']['Begin Date']:
            lt.addLast(namelist, catalog['Artist']['Display Name'])
    
    return namelist

def orgobrasCro(catalog, artwork):
    datelist=lt.newlist()
    artworklist=lt.newlist()
    for artista in catalog['Artworks']:
        fecha=artwork['Date']
        lt.addLast(datelist,fecha)
    ordenado= mg.sort(datelist)
    for fecha in ordenado:
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
    for obra in catalog['Artworks']:
        if obra['Constituent ID'] == encontrarid:
            cantidadobras+=1
            tecnica= obra['Medium']
            encontrartecnica=False
            while encontrartecnica == False:
                if tecnica in tecnicas:
                    lt.addLast(tecnicas[tecnica],obra['Title'])
                    encontrartecnica= True
                else:
                    tecnicas[tecnica]=[]
                    lt.addLast(tecnicas[tecnica],obra['Title'])
                    encontrartecnica= True
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
    for obra in catalog['Artworks']:
        if obra['Title'] in tecnicas[masusada]:
            x=[obra['Title'], obra['Date'], obra['Medium'], obra['Dimensions']]
            obras=[]
            lt.addLast(obras,x)
    return obras

    
