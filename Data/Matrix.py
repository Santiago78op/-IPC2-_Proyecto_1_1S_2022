from Lista.ListaCodDoble import ListaCodDoble
from Constructor.Codigo import Codigo
from Constructor.Piso import Piso
from Constructor.Patron import Patron
from Lista.ListaSimple import PisoListaSimple
from Graphics.GeneraGrafica import Grafica

class Matrix():

    def __init__(self):
        self.cadena = ''
        self.dos_acciones = ''

    def matrix(self,nombrePiso,nombreCod,patron,volteo,intercambio,filas,columnas,lista_b=ListaCodDoble(),lista_c=ListaCodDoble()):
        grafica = Grafica()
        listaPisos = PisoListaSimple()

        nuevoPiso = Piso(nombrePiso, filas, columnas, volteo, intercambio)
        listaPisos.append(nuevoPiso)
        nombreCodigo = f"Patron {nombreCod}"
        nuevoPatron = Patron(nombreCodigo,"En Proceso")
        nuevoPiso.listaPatron.append(nuevoPatron)


        #--------------------------- Algoritmo de Intercambio-Volteo ------------------------------
        voltear = volteo
        intercambiar = intercambio
        cadena = ""
        inter = 0
        volt = 0

        cont_intercambio = 0
        cont_volteo = 0


        total_dos_Acciones = 0


        for f in range(1, int(filas) + 1):
            for c in range(1, int(columnas) + 1):
                letra_c = lista_c.buscarLetra(f, c)
                letra_b = lista_b.buscarLetra(f, c)
                link_b = lista_b.buscarLetra(f, c + 1)
                down_b = lista_b.buscarLetra(f + 1, c)
                link_c = lista_c.buscarLetra(f, c + 1)
                down_c = lista_c.buscarLetra(f + 1, c)

                if letra_b == letra_c:
                    nuevo = nuevoPiso.listaPatron.busquedaPatron(nombreCodigo).listaCodigos
                    if letra_b == nuevo.buscarLetra(f, c):
                        cadena = cadena + "Item no requiere acción.\n"
                    elif nuevo.buscarLetra(f, c) == None:
                        nuevoCodigo = Codigo(letra_c, f, c)
                        nuevoPatron.listaCodigos.append(nuevoCodigo)
                        cadena = cadena + "Item no requiere acción.\n"
                elif letra_b != letra_c:
                    if (lista_b.buscarLetra(f, c + 1) and lista_b.buscarLetra(f + 1, c)) is not None:
                        if (letra_b == link_c and link_b == letra_c):
                            nuevoCodigo = Codigo(link_b, f, c)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            nuevoCodigo = Codigo(letra_b, f, c + 1)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            cadena = cadena + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {link_b, f, c + 1}.\n"
                            inter = inter + intercambiar
                            lista_b.modificar(link_b, f, c)
                            lista_b.modificar(letra_b, f, c + 1)
                            cont_intercambio = cont_intercambio + 1
                        elif (letra_b == down_c and down_b == letra_c):
                            nuevoCodigo = Codigo(down_b, f, c)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            nuevoCodigo = Codigo(letra_b, f + 1, c)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            cadena = cadena + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {down_b, f + 1, c}.\n"
                            inter = inter + intercambiar
                            lista_b.modificar(down_b, f, c)
                            lista_b.modificar(letra_b, f + 1, c)
                            cont_intercambio = cont_intercambio + 1
                        else:
                            nuevoCodigo = Codigo(letra_c, f, c)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            cadena = cadena + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                            volt = volt + voltear
                            cont_volteo = cont_volteo + 1
                    elif (lista_b.buscarLetra(f + 1, c) is not None) and (lista_b.buscarLetra(f, c + 1) is None):
                        if (letra_b == down_c and down_b == letra_c):
                            nuevoCodigo = Codigo(down_b, f, c)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            nuevoCodigo = Codigo(letra_b, f + 1, c)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            cadena = cadena + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {down_b, f + 1, c}.\n"
                            inter = inter + intercambiar
                            lista_b.modificar(down_b, f, c)
                            lista_b.modificar(letra_b, f + 1, c)
                            cont_intercambio = cont_intercambio + 1
                        else:
                            nuevoCodigo = Codigo(letra_c, f, c)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            cadena = cadena + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                            volt = volt + voltear
                            cont_volteo = cont_volteo + 1
                    elif (lista_b.buscarLetra(f + 1, c) is None) and (lista_b.buscarLetra(f, c + 1) is not None):
                        if (letra_b == link_c and link_b == letra_c):
                            nuevoCodigo = Codigo(link_b, f, c)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            nuevoCodigo = Codigo(letra_b, f, c + 1)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            cadena = cadena + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {link_b, f, c + 1}.\n"
                            inter = inter + intercambiar
                            lista_b.modificar(link_b, f, c)
                            lista_b.modificar(letra_b, f, c + 1)
                            cont_intercambio = cont_intercambio + 1
                        else:
                            nuevoCodigo = Codigo(letra_c, f, c)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            cadena = cadena + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                            volt = volt + voltear
                            cont_volteo = cont_volteo + 1
                    elif (lista_b.buscarLetra(f + 1, c) is None) and (lista_b.buscarLetra(f, c + 1) is None):
                        if letra_b == letra_c:
                            nuevoCodigo = Codigo(letra_b, f, c)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            cadena = cadena + "Item no requiere acción.\n"
                        else:
                            nuevoCodigo = Codigo(letra_c, f, c)
                            nuevoPatron.listaCodigos.append(nuevoCodigo)
                            cadena = cadena + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                            volt = volt + voltear
                            cont_volteo = cont_volteo + 1
        total_dos_Acciones = total_dos_Acciones + int(cont_intercambio * intercambio) + int(cont_volteo * volteo)

        letra = str(patron)
        cont = 0
        for f in range(1, int(filas) + 1):
            for c in range(1, int(columnas) + 1):
                l = letra[cont]
                lista_b.modificar(l,f,c)
                cont = cont + 1

        self.dos_acciones = total_dos_Acciones




        # ---------------------------------------  ALGORITMO  ------------------------------------------

    def algoritmo(self,nombrePiso,nombreCod,patron,volteo,intercambio,filas,columnas,lista_b=ListaCodDoble(),lista_c=ListaCodDoble()):
        grafica = Grafica()
        listaPisos = PisoListaSimple()

        # --------------------------- Algoritmo de Operaciones ------------------------------
        num_pisos = int(filas) * int(columnas)
        precio_total_voteo = num_pisos * int(volteo)
        precio_total_intercambio = num_pisos * int(intercambio)
        total_dos_Acciones = self.dos_acciones

        voltear = volteo
        intercambiar = intercambio

        cadena_2 = ""
        inter_2 = 0
        volt_2 = 0


        nuevoPiso_2 = Piso(nombrePiso, filas, columnas, volteo, intercambio)
        listaPisos.append(nuevoPiso_2)
        nombreCodigo_2 = f"Nuevo Patron {nombreCod}"
        nuevoPatron_2 = Patron(nombreCodigo_2, "Replica")
        nuevoPiso_2.listaPatron.append(nuevoPatron_2)

        print(total_dos_Acciones)
        print(precio_total_intercambio)
        print(precio_total_voteo)


        if total_dos_Acciones < precio_total_intercambio and total_dos_Acciones < precio_total_voteo:
            for f in range(1, int(filas) + 1):
                for c in range(1, int(columnas) + 1):
                    letra_c = lista_c.buscarLetra(f, c)
                    letra_b = lista_b.buscarLetra(f, c)
                    link_b = lista_b.buscarLetra(f, c + 1)
                    down_b = lista_b.buscarLetra(f + 1, c)
                    link_c = lista_c.buscarLetra(f, c + 1)
                    down_c = lista_c.buscarLetra(f + 1, c)

                    if letra_b == letra_c:
                        nuevo_2 = nuevoPiso_2.listaPatron.busquedaPatron(nombreCodigo_2).listaCodigos
                        if letra_b == nuevo_2.buscarLetra(f, c):
                            cadena_2 = cadena_2 + "Item no requiere acción.\n"
                        elif nuevo_2.buscarLetra(f, c) == None:
                            nuevoCodigo_2 = Codigo(letra_c, f, c)
                            nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                            cadena_2 = cadena_2 + "Item no requiere acción.\n"
                    elif letra_b != letra_c:
                        if (lista_b.buscarLetra(f, c + 1) and lista_b.buscarLetra(f + 1, c)) is not None:
                            if (letra_b == link_c and link_b == letra_c):
                                nuevoCodigo_2 = Codigo(link_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f, c + 1)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {link_b, f, c + 1}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(link_b, f, c)
                                lista_b.modificar(letra_b, f, c + 1)
                            elif (letra_b == down_c and down_b == letra_c):
                                nuevoCodigo_2 = Codigo(down_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f + 1, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {down_b, f + 1, c}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(down_b, f, c)
                                lista_b.modificar(letra_b, f + 1, c)
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is not None) and (lista_b.buscarLetra(f, c + 1) is None):
                            if (letra_b == down_c and down_b == letra_c):
                                nuevoCodigo_2 = Codigo(down_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f + 1, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {down_b, f + 1, c}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(down_b, f, c)
                                lista_b.modificar(letra_b, f + 1, c)
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is None) and (lista_b.buscarLetra(f, c + 1) is not None):
                            if (letra_b == link_c and link_b == letra_c):
                                nuevoCodigo_2 = Codigo(link_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f, c + 1)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {link_b, f, c + 1}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(link_b, f, c)
                                lista_b.modificar(letra_b, f, c + 1)
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is None) and (lista_b.buscarLetra(f, c + 1) is None):
                            if letra_b == letra_c:
                                nuevoCodigo_2 = Codigo(letra_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + "Item no requiere acción.\n"
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear
        elif precio_total_voteo < total_dos_Acciones and precio_total_voteo < precio_total_intercambio:
            for f in range(1, int(filas) + 1):
                for c in range(1, int(columnas) + 1):
                    letra_c = lista_c.buscarLetra(f, c)
                    letra_b = lista_b.buscarLetra(f, c)
                    link = lista_b.buscarLetra(f, c + 1)
                    down = lista_b.buscarLetra(f + 1, c)

                    if letra_b == letra_c:
                        nuevoCodigo_2 = Codigo(letra_b, f, c)
                        nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                        cadena_2 = cadena_2 + "Item no requiere acción.\n"
                    elif letra_b != letra_c:
                        if (lista_b.buscarLetra(f, c + 1) and lista_b.buscarLetra(f + 1, c)) is not None:
                            nuevoCodigo_2 = Codigo(letra_c, f, c)
                            nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                            cadena_2 = cadena_2 + f"Item requirio la acción Voltear: {letra_b, f, c} por {letra_c, f, c}.\n"
                            volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is not None) and (lista_b.buscarLetra(f, c + 1) is None):
                            nuevoCodigo_2 = Codigo(letra_c, f, c)
                            nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                            cadena_2 = cadena_2 + f"Item requirio la acción Voltear: {letra_b, f, c} por {letra_c, f, c}.\n"
                            volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is None) and (lista_b.buscarLetra(f, c + 1) is not None):
                            nuevoCodigo_2 = Codigo(letra_c, f, c)
                            nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                            cadena_2 = cadena_2 + f"Item requirio la acción Voltear: {letra_b, f, c} por {letra_c, f, c}.\n"
                            volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is None) and (lista_b.buscarLetra(f, c + 1) is None):
                            nuevoCodigo_2 = Codigo(letra_c, f, c)
                            nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                            cadena_2 = cadena_2 + f"Item requirio la acción Voltear: {letra_b, f, c} por {letra_c, f, c}.\n"
                            volt_2 = volt_2 + voltear


        elif precio_total_intercambio < total_dos_Acciones and precio_total_intercambio < precio_total_voteo:
            for f in range(1, int(filas) + 1):
                for c in range(1, int(columnas) + 1):
                    letra_c = lista_c.buscarLetra(f, c)
                    letra_b = lista_b.buscarLetra(f, c)
                    link_b = lista_b.buscarLetra(f, c + 1)
                    down_b = lista_b.buscarLetra(f + 1, c)
                    link_c = lista_c.buscarLetra(f, c + 1)
                    down_c = lista_c.buscarLetra(f + 1, c)

                    if letra_b == letra_c:
                        nuevo_2 = nuevoPiso_2.listaPatron.busquedaPatron(nombreCodigo_2).listaCodigos
                        if letra_b == nuevo_2.buscarLetra(f, c):
                            cadena_2 = cadena_2 + "Item no requiere acción.\n"
                        elif nuevo_2.buscarLetra(f, c) == None:
                            nuevoCodigo_2 = Codigo(letra_c, f, c)
                            nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                            cadena_2 = cadena_2 + "Item no requiere acción.\n"
                    elif letra_b != letra_c:
                        if (lista_b.buscarLetra(f, c + 1) and lista_b.buscarLetra(f + 1, c)) is not None:
                            if (letra_b == link_c and link_b == letra_c):
                                nuevoCodigo_2 = Codigo(link_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f, c + 1)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {link_b, f, c + 1}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(link_b, f, c)
                                lista_b.modificar(letra_b, f, c + 1)
                            elif (letra_b == down_c and down_b == letra_c):
                                nuevoCodigo_2 = Codigo(down_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f + 1, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {down_b, f + 1, c}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(down_b, f, c)
                                lista_b.modificar(letra_b, f + 1, c)
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is not None) and (lista_b.buscarLetra(f, c + 1) is None):
                            if (letra_b == down_c and down_b == letra_c):
                                nuevoCodigo_2 = Codigo(down_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f + 1, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {down_b, f + 1, c}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(down_b, f, c)
                                lista_b.modificar(letra_b, f + 1, c)
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is None) and (lista_b.buscarLetra(f, c + 1) is not None):
                            if (letra_b == link_c and link_b == letra_c):
                                nuevoCodigo_2 = Codigo(link_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f, c + 1)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {link_b, f, c + 1}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(link_b, f, c)
                                lista_b.modificar(letra_b, f, c + 1)
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is None) and (lista_b.buscarLetra(f, c + 1) is None):
                            if letra_b == letra_c:
                                nuevoCodigo_2 = Codigo(letra_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + "Item no requiere acción.\n"
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear



        elif precio_total_intercambio == precio_total_voteo:
            for f in range(1, int(filas) + 1):
                for c in range(1, int(columnas) + 1):
                    letra_c = lista_c.buscarLetra(f, c)
                    letra_b = lista_b.buscarLetra(f, c)
                    link_b = lista_b.buscarLetra(f, c + 1)
                    down_b = lista_b.buscarLetra(f + 1, c)
                    link_c = lista_c.buscarLetra(f, c + 1)
                    down_c = lista_c.buscarLetra(f + 1, c)

                    if letra_b == letra_c:
                        nuevo_2 = nuevoPiso_2.listaPatron.busquedaPatron(nombreCodigo_2).listaCodigos
                        if letra_b == nuevo_2.buscarLetra(f, c):
                            cadena_2 = cadena_2 + "Item no requiere acción.\n"
                        elif nuevo_2.buscarLetra(f, c) == None:
                            nuevoCodigo_2 = Codigo(letra_c, f, c)
                            nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                            cadena_2 = cadena_2 + "Item no requiere acción.\n"
                    elif letra_b != letra_c:
                        if (lista_b.buscarLetra(f, c + 1) and lista_b.buscarLetra(f + 1, c)) is not None:
                            if (letra_b == link_c and link_b == letra_c):
                                nuevoCodigo_2 = Codigo(link_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f, c + 1)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {link_b, f, c + 1}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(link_b, f, c)
                                lista_b.modificar(letra_b, f, c + 1)
                            elif (letra_b == down_c and down_b == letra_c):
                                nuevoCodigo_2 = Codigo(down_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f + 1, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {down_b, f + 1, c}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(down_b, f, c)
                                lista_b.modificar(letra_b, f + 1, c)
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is not None) and (lista_b.buscarLetra(f, c + 1) is None):
                            if (letra_b == down_c and down_b == letra_c):
                                nuevoCodigo_2 = Codigo(down_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f + 1, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {down_b, f + 1, c}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(down_b, f, c)
                                lista_b.modificar(letra_b, f + 1, c)
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is None) and (lista_b.buscarLetra(f, c + 1) is not None):
                            if (letra_b == link_c and link_b == letra_c):
                                nuevoCodigo_2 = Codigo(link_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                nuevoCodigo_2 = Codigo(letra_b, f, c + 1)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion Intercambio: {letra_b, f, c} switch {link_b, f, c + 1}.\n"
                                inter_2 = inter_2 + intercambiar
                                lista_b.modificar(link_b, f, c)
                                lista_b.modificar(letra_b, f, c + 1)
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear
                        elif (lista_b.buscarLetra(f + 1, c) is None) and (lista_b.buscarLetra(f, c + 1) is None):
                            if letra_b == letra_c:
                                nuevoCodigo_2 = Codigo(letra_b, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + "Item no requiere acción.\n"
                            else:
                                nuevoCodigo_2 = Codigo(letra_c, f, c)
                                nuevoPatron_2.listaCodigos.append(nuevoCodigo_2)
                                cadena_2 = cadena_2 + f"Item requirio la accion volteo: {letra_b, f, c} switch {letra_c, f, c}.\n"
                                volt_2 = volt_2 + voltear

        nuevoPiso_2.listaPatron.busquedaPatron(nombreCodigo_2).listaCodigos.recorrerCodigo()


        lista = nuevoPiso_2.listaPatron.busquedaPatron(nombreCodigo_2).listaCodigos
        grafica.graphic(nombrePiso,filas,columnas,nombreCod,lista)

        costoM_2 = inter_2 + volt_2
        cadena_2 = cadena_2 + "\n El costo Minimo de esta Accion es: " + str(costoM_2)
        ruta = 'Graphics\\Instrucciones.txt '
        file = open(ruta, 'w')
        file.write(f"{cadena_2}")
        file.close()

        self.cadena = cadena_2

        letra = str(patron)
        cont = 0
        for f in range(1, int(filas) + 1):
            for c in range(1, int(columnas) + 1):
                l = letra[cont]
                lista_b.modificar(l,f,c)
                cont = cont + 1

    def retornoCadena(self):
        return self.cadena








