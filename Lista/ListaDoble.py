from Constructor.Patron import Patron

class PatronListaDoble():

    def __init__(self):
        self.raiz = Patron()
        self.ultimo = self.raiz


    def append(self, nuevoPatron):
        if self.raiz.patron is None:
            self.raiz = nuevoPatron
        elif self.raiz.nodo.link is None:
            self.raiz.nodo.link = nuevoPatron
            nuevoPatron.nodo.previous = self.raiz
            self.ultimo = nuevoPatron
        else:
            self.ultimo.nodo.link = nuevoPatron
            nuevoPatron.nodo.previous = self.ultimo
            self.ultimo = nuevoPatron


    def printDoblePatron(self):
        nodoAux = self.raiz

        cadena = ''
        encabezado = ''
        while True:
            if nodoAux.patron is not None:
                cadena += "(" +" Codigo: "+nodoAux.codigo + " " +"Patron: "+nodoAux.patron + ")"
                if nodoAux.nodo.link is not None:
                    encabezado += "  -> "
                    cadena += " -> "
                    nodoAux = nodoAux.nodo.link
                else:
                    break
            else:
                break
        print(cadena)

    def sortDoubleListPatron(self):
        if self.raiz == None:
            return
        else:
            current = self.raiz
            while current.nodo.link:
                index = current.nodo.link
                while index != None:
                    if current.codigo > index.codigo:
                        temp = current.codigo
                        current.codigo = index.codigo
                        index.codigo = temp
                    index = index.nodo.link
                current = current.nodo.link

    def buscarPatron(self,codigo):
        current = self.raiz

        while current and current.codigo != codigo:
            current = current.nodo.link

        if current is None:
            return None
        elif current:
            return current