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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initDatos():
    catalog= model.iniciarDatos()
    return catalog

catalog= initDatos()

# Funciones para la carga de datos

def cargarDatos(catalog):

    loadArtist(catalog)
    loadArtworks(catalog)

def loadArtist(catalog):
    artistfile= cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file= csv.DictReader(open(artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    artworksfile= cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file= csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

# Funciones de ordenamiento

def getartistasCro(catalog, artist):
    artistasCro= model.orgartistasCro(catalog, artist)
    return artistasCro
def getobrasCro(catalog, artwork):
    obrasCro= model.orgobrasCro(catalog, artwork)
    return obrasCro


# Funciones requerimiento 1
def getorgartistascro(catalog, inicial, final):
    artistas= model.orgartistasCro(catalog,inicial,final)
    return artistas

def getordenarArtistas(artistas):
    ordenada= model.ordenarArtistas(artistas)
    return ordenada

def getprimeros3(ordenada):
    primeros= model.primeros3(ordenada)
    return primeros

def  getultimos3(ordenada):
    ultimos= model.ultimos3(ordenada)
    return ultimos

# Funciones requerimiento 2
def getcompararIDayo(catalog, id):
    nomArtista= model.compararIDayo(catalog, id)
    return nomArtista
def getorgObrasCro(catalog, inicial, final):
    tupla= model.orgObrasCro(catalog, inicial, final)
    return tupla
def getordenarObras(obras):
    ordenada= model.ordenarObras(obras)
    return ordenada
def getnumPurchase(catalog):
    conteoPu= model.numPurchase(catalog)
    return conteoPu

# Funciones requerimiento 3
def getenconID(catalog, nombre):
    encontrarid= model.enconID(catalog, nombre)
    return encontrarid
def gettecnicasartista(catalog, encontrarid):
    tecnicasyobras= model.tecnicasartista(atalog, encontrarid)
    return tecnicasyobras
def getcantidadtecnicas(tecnicas):
    totalTecni= model.cantidadtecnicas(tecnicas)
    return totalTecni
def gettecnimasusada(tecnicas:dict):
    masusada= model.tecnimasusada(tecnicas:dict)
    return masusada
def getlistaObras(catalog, masusada, tecnicas):
    obras= model.listaObras(catalog, masusada, tecnicas)
    return obras
# Funciones requerimiento 4
def getidArtists(catalog):
    id=model.idArtists(catalog)
    return id
def getidyNacio(catalog, id):
    nacioNombre= model.idyNacio(catalog, id)
    return nacioNombre
def getcontNacio(catalog, nacioNombre: dict):
    nacioNombre= model.contNacio(catalog, nacioNombre: dict)
    return nacioNombre
def getTop10(nacioNombre: dict):
    top10= model.Top10(nacioNombre: dict)
    return top10
def getnacioMasObras(top10, catalog):
    obrasNa= model.nacioMasObras(top10, catalog)
    return obrasNa
def getlista_nacionalidades(nacioNombre: dict):
    lst_top10_final=model.lista_nacionalidades(nacioNombre: dict)
    return lst_top10_final
# Funciones requerimiento 5
def getobrasDepartamento(departamento, catalog):
    lista= model.obrasDepartamento(departamento, catalog)
    return lista
def getlistafechas(lista):
    listafechas= model.listafechas(lista)
    return listafechas
def getordenar(o1,o2):
    orden=model.ordenar(o1,o2)
    return orden
def getordenarlista(listafechas):
    listaordenada=model.ordenarlista(listafechas)
    return listaordenada
def getlistaprecios(costoObras:dict):
    listaprecios= model.listaprecios(costoObras:dict)
    return listaprecios
def getordenar2(o1,o2):
    orden2= model.ordenar2(o1,o2)
    return orden2
def getordenarlista2(listafechas):
    listaOrdenadaprecios2= model.ordenarlista(listafechas)
    return listaOrdenadaprecios2
def getlistaprecios(costoObras:dict):
def getordenar(o1,o2):
def getordenarlista(listaprecios):
def getpesototal(lista):
def getcantidadObras(lista):
def getdictCostos(lista):
def getcostoEstimado(costoObras:dict):
def getobrasMasAntiguas(listaOrdenada, catalog, lista):
def getobrasMasCost(listaOrdenadaprecios, catalog, lista):