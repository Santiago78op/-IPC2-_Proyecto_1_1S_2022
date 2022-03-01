from Nodo.NodoSimple import NodoSimple
from Lista.ListaDoble import PatronListaDoble
 
class Piso():

    def __init__(self, piso=None,fila=None,columna=None,volteo=None,intercambiar=None):
        self.piso = piso
        self.fila = fila
        self.columna = columna
        self.volteo = volteo
        self.intercambiar = intercambiar
        self.nodo = NodoSimple()
        self.listaPatron = PatronListaDoble()
