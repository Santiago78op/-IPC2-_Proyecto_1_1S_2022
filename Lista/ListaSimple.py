from Nodo.NodoSimple import NodoSimple

class PisoListaSimple():

    def __init__(self,nodecount=0):
        self.head = None
        self.nodecount = nodecount


    def append(self, nuevoPiso):
        if self.head is None:
            self.head = NodoSimple(data=nuevoPiso)
            self.nodecount = self.nodecount + 1
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = NodoSimple(data=nuevoPiso)
        self.nodecount = self.nodecount + 1


    def recorrerPiso(self):
        current = self.head

        while current != None:
            print("Piso: ",current.data.piso," Filas: ",current.data.fila," Columna: ",current.data.columna)
            current = current.link

    def busquedaPiso(self,piso):
        if self.head is None:
            print("El piso no existe en el Archivo!!")
            return
        current = self.head

        while current is not None:
            if current.data.piso == piso:
                return current.data
            current = current.link
        print("Item no Encontrado")
        return None

    def bubbleSortPisos(self):
        for i in range(self.nodecount-1):
            curr = self.head
            nxt = curr.link
            prev = None
            while nxt:
                if curr.data.piso > nxt.data.piso:
                    if prev == None:
                        prev = curr.link
                        nxt = nxt.link
                        prev.link = curr
                        curr.link = nxt
                        self.head = prev
                    else:
                        temp = nxt
                        nxt = nxt.link
                        prev.link = curr.link
                        prev = temp
                        temp.link = curr
                        curr.link = nxt
                else:
                    prev=curr
                    curr=nxt
                    nxt=nxt.link
            i=i+1




