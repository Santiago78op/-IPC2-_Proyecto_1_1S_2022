from Nodo.DoubleLinkedList import *

class Atributos:

    def redesign(self,titulo,lista):
        for p in lista:
            piso = p[0]
            columna = p[1]
            celda = p[2]
            volteo = p[3]
            intercambio = p[4]
            contenedor_patron = p[5:]
            for i in contenedor_patron:
                codigo = i[0]
                secuencia = i[1]
            patron = Patron(codigo,secuencia)
            piso = Pisos(piso,columna,celda,volteo,intercambio,patron)
            lista_p = lista_pisos()
            lista_p.insertar(piso)
            lista_p.recorrer()
