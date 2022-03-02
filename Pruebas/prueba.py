from operator import itemgetter

lista = [['Segundo Piso', ' 2 ', ' 4 ', ' 1 ', ' 1 ', ['ppp12', 'WBWBWWWB'], ['ttt24', 'BWBWWWWW']], ['Primer Piso', ' 3 ', ' 3 ', ' 1 ', ' 1 ', ['jjj26', 'WBBBWBWWW'], ['aaa97', 'WWWWBWWWB']], ['Cuarto Piso', ' 1 ', ' 5 ', ' 1000 ', ' 1 ', ['cod31', 'WBBBB'], ['cod35', 'BBBWW']]]

variable = (sorted(lista, key=itemgetter(0)))
print(variable)

#varaible = (sorted(ordenar, key=itemgetter(0)))

#print(varaible)
#contenedor_piso[0][len(contenedor_piso[0]):]=[[codigo,num_patron]]

#C:\Users\santi\PyCharmProyect\IPC2\Proyecto_1\app\Pruebas\prueba_piso1.xml
#https://fathomless-dawn-11616.herokuapp.com/analizar
#C:\\Users\\santi\\PyCharmProyect\\IPC2\\Proyecto_1\\app\\
"""
    contenedor_piso.append([nombre_piso,R.childNodes[0].data,C.childNodes[0].data,F.childNodes[0].data,S.childNodes[0].data])

            for i in range(contador_piso):
                contenedor_piso[i].append(contenedor)
            print(contenedor_piso)
"""

"""
            piso = p[0]
            columna = p[1]
            celda = p[2]
            volteo = p[3]
            intercambio = p[4]
            cont_patron = p[5:]
            orden = (sorted(cont_patron, key=itemgetter(0)))
            patrones = Patron(orden)
            piso = Pisos(titulo,piso,columna,celda,volteo,intercambio,patrones)
            lista_p = lista_pisos()
            lista_p.insertar(piso)
            lista_p.recorrer()
"""
"""
class ListaSimpleEnlazada():

    # Function to initialize head
    def __init__(self):
        self.head = Piso()
        self.last = self.head


    def append(self, nuevoPiso):
        if self.head.piso is None:
            self.head = nuevoPiso
        elif self.head.nodo.link is None:
            self.head.nodo.link = nuevoPiso
            self.last = nuevoPiso
        else:
            self.last.nodo.link = nuevoPiso
            self.last = nuevoPiso

    def printListaSimpleEnlazada(self):
        nodoAux = self.head

        cadena = ''
        while True:
            if nodoAux.piso is not None:
                cadena += "(" + nodoAux.piso + " " + nodoAux.fila + " " + nodoAux.columna + " " + nodoAux.volteo + " " + nodoAux.intercambiar + ")"
                if nodoAux.nodo.link is not None:
                    cadena += " -> "
                    nodoAux = nodoAux.nodo.link
                else:
                    break
            else:
                break
        print(cadena)

    def bubbleSort(self):
        for i in range(self.nodecount-1):
            curr = self.head
            nxt = curr.link
            prev = None
            while nxt:
                if curr.data.carne > nxt.data.carne:
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
"""
"""
class ListaDobleEnlazada():

    def __init__(self):
        self.head = Patron()
        self.last = self.head

    def append(self, nuevoPatron):
        if self.head.codigo is None:
            self.head = nuevoPatron
        elif self.head.nodo.link is None:
            self.head.nodo.link = nuevoPatron
            nuevoPatron.nodo.previous = self.head
            self.last = nuevoPatron
        else:
            self.last.nodo.link = nuevoPatron
            nuevoPatron.nodo.previous = self.last
            self.last = nuevoPatron

    def printDobleEnlazada(self):
        nodoAux = self.head

        cadena = ''
        while True:
            if nodoAux.codigo is not None:
                cadena += "(" + nodoAux.codigo + " " + nodoAux.patron + ")"
                if nodoAux.nodo.link is not None:
                    cadena += " -> "
                    nodoAux = nodoAux.nodo.link
                else:
                    break
            else:
                break
        print(cadena)

    def sort_patron(self):
        if self.head == None:
          return
        else:
          current = self.head
          while current.nodo.link != None:
            index = current.nodo.link
            while index != None:
              if current.codigo > index.codigo:
                temp = current
                current = index
                index= temp
              index = index.nodo.link
            current = current.nodo.link
"""