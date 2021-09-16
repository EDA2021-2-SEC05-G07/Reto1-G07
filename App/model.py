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
def cargarDatos():
    catalog={'Artists': None, 'ArtWorks': None}

    catalog['Artists']= lt.newlist()
    catalog['Artwors']= lt.newlist('ARRAY_LIST', "llama funcion para comparar")

    return catalog

def addArtist(catalog, artist):
    info= artist.split(sep=',')
    ar= artist['Display Name'], artist['Gender'], artist['Nationality'], artist['Begin Date']
    lt.addLast(catalog['Artists'], ar)

def addArtwork(catalog, artwork):
    at= artwork['Medium'], artwork['Title']
    lt.addLast(catalog['Artworks'],at)


# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def orgartistasCro(catalog, artist):
    datelist=lt.newlist()
    namelist=lt.newlist()
    for artista in catalog['Artist']:
        fecha=artist['Begin Date']
        lt.addLast(datelist,fecha)
    ordenado= mg.sort(datelist)
    for fecha in ordenado:
        if fecha == catalog['Artist']['Begin Date']:
            lt.addLast(namelist, catalog['Artist']['Display Name'])
    
    return namelist

def orgobrasCro(catalog, artwork):
    datelist=lt.newlist()
    artworklist=lt.newlist()
    for artista in catalog['Artwork']:
        fecha=artwork['Date']
        lt.addLast(datelist,fecha)
    ordenado= mg.sort(datelist)
    for fecha in ordenado:
        if fecha == catalog['Artwork']['Date']:
            lt.addLast(artworklist, catalog['Artwork']['Title'])
    
    return artworklist


    
