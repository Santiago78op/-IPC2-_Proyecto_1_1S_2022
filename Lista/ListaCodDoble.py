from Nodo.NodoDobleCod import NodoDobleCod

class ListaCodDoble():

    def __init__(self):
        self.head = None


    def append(self, nuevoCod):
        if self.head is None:
            self.head = NodoDobleCod(data=nuevoCod)
        else:
            current = NodoDobleCod(data=nuevoCod,link=self.head)
            self.head.previous = current
            self.head = current

    def buscarLetra(self,fila,columna):
        current = self.head
        flag = False
        if self.head == None:
            return None

        while current != None:
            if current.data.fila == fila and current.data.columna == columna:
                flag = True
                return current.data.letra
                break
            current = current.link

    def recorrerCodigo(self):
        if self.head is None:
            return
        current = self.head
        print("Letra: ",current.data.letra," Fila: ", current.data.fila," Columna: ", current.data.columna)

        while current.link:
            current = current.link
            print("Letra: ",current.data.letra," Fila: ", current.data.fila," Columna: ", current.data.columna)



