from Nodo.NodoDoble import NodoDoble
from Lista.ListaCodDoble import ListaCodDoble

class Patron():

    def __init__(self, codigo=None, patron=None):
        self.codigo = codigo
        self.patron = patron
        self.nodo = NodoDoble()
        self.listaCodigos = ListaCodDoble()

