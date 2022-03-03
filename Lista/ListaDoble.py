from Nodo.NodoDoble import NodoDoble

class PatronListaDoble():

    def __init__(self):
        self.head = None


    def append(self, nuevoPatron):
        if self.head is None:
            self.head = NodoDoble(data=nuevoPatron)
        else:
            current = NodoDoble(data=nuevoPatron,link=self.head)
            self.head.previous = current
            self.head = current


    def recorrerPatron(self):
        if self.head is None:
            return
        current = self.head
        print("Codigo: ",current.data.codigo," Patron: ", current.data.patron)

        while current.link:
            current = current.link
            print("Codigo: ", current.data.codigo, " Patron: ", current.data.patron)


    def busquedaPatron(self, codigo):
        current = self.head

        while current and current.data.codigo != codigo:
            current = current.link

        if current is None:
            print("El Codigo no Existe en el Piso")
            return None
        elif current:
            return current.data

    def sortPatron(self):
        if self.head == None:
            return
        else:
            current = self.head
            while current.link != None:
                index = current.link
                while index != None:
                    if current.data.codigo > index.data.codigo:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.link
                current = current.link


