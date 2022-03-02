from Constructor.Codigo import Codigo

class ListaCodDoble():

    def __init__(self):
        self.raiz = Codigo()
        self.ultimo = self.raiz


    def append(self, nuevoCod):
        if self.raiz.letra is None:
            self.raiz = nuevoCod
        elif self.raiz.nodo.link is None:
            self.raiz.nodo.link = nuevoCod
            nuevoCod.nodo.previous = self.raiz
            self.ultimo = nuevoCod
        else:
            self.ultimo.nodo.link = nuevoCod
            nuevoCod.nodo.previous = self.ultimo
            self.ultimo = nuevoCod

    def printDobleCod(self):
        nodoAux = self.raiz

        cadena = ''
        while True:
            if nodoAux.letra is not None:
                cadena += "(" +" letra: "+str(nodoAux.letra) + " " +"fila: "+str(nodoAux.fila) +" " +"Columna: "+ str(nodoAux.columna)+ ")"
                if nodoAux.nodo.link is not None:
                    cadena += " \n "
                    nodoAux = nodoAux.nodo.link
                else:
                    break
            else:
                break
        print(cadena)


    def buscarLetra(self, fila,columna):
        nodoAux = self.raiz

        while (nodoAux.fila != fila and nodoAux.columna != columna):
            if nodoAux.nodo.link is not None:
                nodoAux = nodoAux.nodo.link
            else:
                return None
        return nodoAux
