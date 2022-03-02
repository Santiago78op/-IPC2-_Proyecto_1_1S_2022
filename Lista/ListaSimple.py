from Constructor.Piso import Piso

class PisoListaSimple():

    def __init__(self):
        self.raiz = Piso()
        self.ultimo = self.raiz


    def append(self, nuevoPiso):
        if self.raiz.piso is None:
            self.raiz = nuevoPiso
        elif self.raiz.nodo.link is None:
            self.raiz.nodo.link = nuevoPiso
            self.ultimo = nuevoPiso
        else:
            self.ultimo.nodo.link = nuevoPiso
            self.ultimo = nuevoPiso


    def printSimplePiso(self):
        nodoAux = self.raiz

        cadena = ''
        while True:
            if nodoAux.piso is not None:
                cadena += "(" + nodoAux.piso + ")"
                if nodoAux.nodo.link is not None:
                    cadena += " -> "
                    nodoAux = nodoAux.nodo.link
                else:
                    break
            else:
                break
        print(cadena)


    def sortSimpleListPisos(self):
        current = self.raiz
        index = None

        if self.raiz == None:
            return
        else:
            while current != None:
                index = current.nodo.link
                while index != None:
                    if current.piso > index.piso:
                        temp = current
                        current = index
                        index = temp
                    index = index.nodo.link
                current = current.nodo.link


    def buscarPiso(self,piso):
        nodoAux = self.raiz

        while nodoAux.piso != piso:
            if nodoAux.nodo.link is not None:
                nodoAux = nodoAux.nodo.link
            else:
                return None
        return nodoAux

