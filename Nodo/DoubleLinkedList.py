class Patron:

    def __init__(self, codigo, num_patron):
        self.codigo = codigo
        self.num_patron = num_patron

class Pisos:

    def __init__(self, titulo, columna, celda, volteo_azulejo, intercambio_azulejo, patron):
        self.titulo = titulo
        self.columna = columna
        self.celda = celda
        self.volteo_azulejo = volteo_azulejo
        self.intercambio_azulejo = intercambio_azulejo
        self.patron = patron

class Nodo:

    def __init__(self, data=None, link=None, previous=None):
        self.data = data
        self.link = link
        self.previous = previous


class lista_pisos:

    def __init__(self):
        self.head = None

    def insertar(self, piso):
        if self.head is None:
            self.head = Nodo(data=piso)
        else:
            current = Nodo(data=piso, link = self.head)
            self.head.previous = current
            self.head = current

    def recorrer(self):
        if self.head is None:
            return
        current = self.head
        print("Nombre Piso: ", current.data.titulo)
        while current.link:
            current = current.link
            print("Nombre Piso: ", current.data.titulo)
