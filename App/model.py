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


from DISClib.DataStructures.arraylist import addLast
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
#Carga de datos
def iniciarDatos():
    catalog={'Artists': None, 'Artworks': None}

    catalog['Artists']= lt.newList()
    catalog['Artworks']= lt.newList()

    return catalog

def addArtist(catalog, artist):
    lt.addLast(catalog['Artists'], artist)

def addArtwork(catalog, artwork):
    lt.addLast(catalog['Artworks'],artwork)

#Requerimiento 1

def orgartistasCro(catalog, inicial, final):
    artistas=lt.newList()
    for artista in lt.iterator(catalog['Artists']):
        if artista['BeginDate']>= inicial and artista['BeginDate']<= final:
            informacion= lt.newList()
            lt.addLast(informacion, artista['DisplayName'])
            lt.addLast(informacion, artista['BeginDate'])
            lt.addLast(informacion, artista['EndDate'])
            lt.addLast(informacion, artista['Nationality'])
            lt.addLast(informacion, artista['Gender'])
            lt.addLast(artistas,informacion)
    return artistas

def ordenarArtistas(artistas):
    ordenada= ordenarlista(artistas, ordenar)
    return ordenada

def primeros3(ordenada):
    return lt.subList(ordenada, 1, 3)

def ultimos3(ordenada):
    return lt.subList(ordenada, (lt.size(ordenada))-3, 3)

#Requerimiento 2
def compararIDayo(catalog, id):
    #en id entraria el constituent ID del artworks
    for artist in lt.iterator(catalog['Artist']):
        if id == artist['ConstituentID']:
            nomArtista = artist['DisplayName']
            return nomArtista

def orgObrasCro(catalog, inicial, final):
    obras =lt.newList()
    conteoObras = 0
    for obra in lt.iterator(catalog['Artwoks']):        
        if obra['DateAcquired']>= inicial and obra['DateAcquired']<= final:
            conteoObras += 1
            informacion= lt.newList()
            lt.addLast(informacion, obra['Title'])
            lt.addLast(informacion, obra[compararIDayo(obra['ConstituentID'])])
            lt.addLast(informacion, obra['Date'])
            lt.addLast(informacion, obra['DateAcquired'])
            lt.addLast(informacion, obra['Medium'])
            lt.addLast(informacion, obra['Dimensions'])
            lt.addLast(obras,informacion)
    tupla = (obras, conteoObras)
    """
    obras->tupla[0], obras es la lista de las obras en el rango
    conteoObras->tupla[1], conteoObras es el numero de obras en el rango
    """
    return tupla

def ordenarObras(obras):
    ordenada= ordenarlista(obras)
    return ordenada

def numPurchase(catalog):
    conteoPu = 0
    for obra in lt.iterator(catalog['Artworks']):
        if obra['CreditLine'] == 'Purchase':
            conteoPu += 1
        return conteoPu
#para sacar las primeras y ultimas 3 obras se puede usar las funciones
#primeros3 y ultimos3 de req1

#Requerimiento 3

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
            info=lt.newList()
            lt.addLast(info, obra['Title'])
            lt.addLast(info, obra['Date'])
            lt.addLast(info, obra['Medium'])
            lt.addLast(info, obra['Dimensions'])
            obras=lt.newList()
            lt.addLast(obras,info)
    return obras

#Requerimiento 4

def obrasnacionalidad(catalog):
    lst_obras_na = {}
    for obra in lt.iterator(catalog['Artworks']):
        nacionalidad = obra['Nationality']
        lst_obras_na[nacionalidad] = ''
        x= lt.newList
        lt.addLast(x, obra['Title'])
        lt.addLast(x, obra['Date'])
        lt.addLast(x, obra['Medium'])
        lt.addLast(x, obra['Dimensions'])
        lt.addLast(x, obra[compararIDayo(obra['ConstituentID'])])
        if nacionalidad in lst_obras_na:
                lst_obras_na[nacionalidad] = x
        else:
                lst_obras_na[nacionalidad]= x
    return lst_obras_na

def nombreArtista(catalog, id):
    encontro= False
    while encontro == False:
        if id == catalog['Artists']['ConstituentID']:
            nombre= catalog['Artists']['DisplayName']
    return nombre
#no se usa
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

#def nacio_mayor_obras(catalog, lst_top10_final):
 #   for lt.iterator(catalog['Artworks']):
  #  return None

    

#Requerimiento 5 

def obrasDepartamento(departamento, catalog):
    lista= lt.newList()
    for obra in lt.iterator(catalog['Artworks']):
        if catalog['Artworks']['Department'] == departamento:
            lt.addLast(lista, obra)
    return lista
def ordenar(o1,o2,categoria):
    return o1[categoria]<o2[categoria]

def ordenarlista(lista):
    listaOrdenada=sa.sort(lista, ordenar)
    return listaOrdenada

def pesototal(lista):
    peso=0
    for obra in lt.iterator(lista):
        pesoObra= int(obra['Weight'])
        peso+= pesoObra
    return peso

def cantidadObras(lista):
    totalObras= lt.size(lista)
    return totalObras

def dictCostos(lista):
    costoObras={}
    for obra in lt.iterator(lista):
        altura=obra['Height']
        longitud=obra['Length']
        peso=obra['Weigth']
        ancho= obra['Width']
        if (altura== '' or longitud=='') and peso=='':
            costoObras[obra['Title']]= 48
        else:
            mayor=0
            costos=lt.newList()
            if longitud != '' and altura!= '':
                area= (altura*longitud)/100
                precioArea= 72/area
                lt.addLast(costos, precioArea)
                if ancho!='':
                    volumen= (altura*longitud*ancho)/100
                    precioVolumen= 72/volumen
                    lt.addLast(costos, precioVolumen)
            if peso != '':
                precioPeso= 72/peso
                lt.addLast(costos, precioPeso)
            for precio in lt.iterator(costos):
                if precio> mayor:
                    mayor= precio
            costoObras[obra['Title']]= mayor
    return costoObras

def costoEstimado(costoObras):
    suma=sum(costoObras.values())
    return suma

def obrasMasAntiguas(listaOrdenada, catalog):
    x= lt.subList(listaOrdenada, (lt.size(listaOrdenada))-5, 5)
    masAntiguas= lt.newList()
    for obra in lt.iterator(x):
        info= lt.newList()
        lt.addLast(info, obra['Title'])
        id= obra['ConstituentID']
        artista = compararIDayo(id)
        #artista=nombreArtista(catalog, id)
        lt.addLast(info, artista)
        lt.addLast(info, obra['Classification'])
        lt.addLast(info, obra['Date'])
        lt.addLast(info, obra['Medium'])
        lt.addLast(info, obra['Dimensions'])
        costotransporte= costoEstimado(listaOrdenada)
        for llave in costotransporte.keys():
            if llave == obra['Title']:
                costo=costotransporte[llave]
                break
        lt.addLast(info, costo)
        lt.addLast(masAntiguas, info)
    return masAntiguas 

def obrasMasCost(listaOrdenada, catalog):
    x= lt.subList(listaOrdenada, (lt.size(listaOrdenada))-5, 5)
    masCost= lt.newList()
    for obra in lt.iterator(x):
        info= lt.newList()
        lt.addLast(info, obra['Title'])
        id= obra['ConstituentID']
        artista = compararIDayo(id)
        #artista=nombreArtista(catalog, id)
        lt.addLast(info, artista)
        lt.addLast(info, obra['Classification'])
        lt.addLast(info, obra['Date'])
        lt.addLast(info, obra['Medium'])
        lt.addLast(info, obra['Dimensions'])
        costotransporte= costoEstimado(listaOrdenada)
        for llave in costotransporte.keys():
            if llave == obra['Title']:
                costo=costotransporte[llave]
                break
        lt.addLast(info, costo)
        lt.addLast(masCost, info)
    return masCost