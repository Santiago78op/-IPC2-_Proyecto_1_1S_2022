import os
from colorama import Fore
from Data.Lectura import Analizador
from Constructor.Patron import Patron
from Constructor.Piso import Piso
from Constructor.Codigo import Codigo
from Lista.ListaSimple import PisoListaSimple
import xml.etree.ElementTree as ET
from Graphics.GeneraGrafica import Grafica
from Data.Matrix import Matrix

class Menu():

    def __init__(self):
        self.cargar = 1
        self.graficar_patron = 2
        self.cambiar_patron = 3
        self.imprimir = 4
        self.salir = 0

    def mostrar_menu(self) -> None:
        """
        Función que limpia la pantalla y muestra nuevamente el menu
        """
        os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
        print(Fore.CYAN,f'''\t<--Menu Principal-->\n
Selecciona una opción:\n
    \t{self.cargar }) - Cargar Archivo 
    \t{self.graficar_patron}) - Graficar Patron
    \t{self.cambiar_patron}) - Cambiar Patron
    \t{self.imprimir}) - Imprimir Acción
    \t{self.salir}) - Salir\n''')

    def menu(self) -> bool:
        infodata = Analizador()
        grafica = Grafica()
        matriz = Matrix()


        while True:

            self.mostrar_menu()

            opcionMenu = input("Inserta el numero de la opcion: >> ")

            try:
                opcionMenu = int(opcionMenu)

                os.system('cls')

                if opcionMenu == self.cargar:
                    carga = input("Inserta la ruta del archivo .xml: >> \n")
                    ruta = infodata.Leer(carga)
                    nuevaRuta = infodata.guardar(ruta)
                    listaPisos = self.readXML(nuevaRuta)
                    print(Fore.LIGHTWHITE_EX + "\nSe Cargo el Archivo con Exito!")

                elif opcionMenu == self.graficar_patron:
                    opcPiso = ''

                    while opcPiso != '0':
                        print(Fore.BLUE, "Graficar Patron\n")
                        print(Fore.BLUE, "1) -> Buscar Piso")
                        print(Fore.BLUE, "0) -> Salir")

                        opcPiso = input("\nIngresa Opción: ")

                        if opcPiso == '1':
                            print(Fore.LIGHTGREEN_EX, "Listado de Pisos A-Z")
                            listaPisos.bubbleSortPisos()
                            listaPisos.recorrerPiso()

                            nombrePiso = input("\nInserta el Piso: ")
                            piso = listaPisos.busquedaPiso(nombrePiso)
                            if piso == None:
                                print(Fore.RED,"No Existe el Piso Error!")
                            else:
                                print("Piso: ", piso.piso, " Filas: ", piso.fila, " Columna: ",piso.columna)
                                print(Fore.LIGHTCYAN_EX,"El Piso fue encontrado con Exito!!!!!\n")
                                piso.listaPatron.sortPatron()
                                piso.listaPatron.recorrerPatron()

                                nombreCodigo = input("\nInserta el Codigo a Graficar: ")
                                codigo = piso.listaPatron.busquedaPatron(nombreCodigo)
                                if codigo == None:
                                    print(Fore.RED, "No Existe el Codigo Error!")
                                else:
                                    print(Fore.LIGHTMAGENTA_EX, "\nEl Patron a Trabajar es: \n")
                                    print(Fore.LIGHTGREEN_EX, "Codigo: ", codigo.codigo)
                                    print(Fore.LIGHTGREEN_EX, "Patron: ", codigo.patron,"\n")
                                    codigo.listaCodigos.recorrerCodigo()
                                    fila = piso.fila
                                    columna = piso.columna
                                    lista = piso.listaPatron.busquedaPatron(nombreCodigo).listaCodigos
                                    grafica.graphic(nombrePiso,fila,columna,nombreCodigo,lista)

                elif opcionMenu == self.cambiar_patron:
                    opcPiso = ''

                    while opcPiso != '0':
                        print(Fore.BLUE, "Graficar Patron\n")
                        print(Fore.RED, "Seleccione el Patron Base el cual "
                                        "se Modificara al Patron Cambiar\n")
                        print(Fore.BLUE, "1) -> Buscar Piso")
                        print(Fore.BLUE, "0) -> Salir")

                        opcPiso = input("\nIngresa Opción: ")

                        if opcPiso == '1':
                            print(Fore.LIGHTGREEN_EX, "Listado de Pisos A-Z")
                            listaPisos.bubbleSortPisos()
                            listaPisos.recorrerPiso()

                            pisoBase = input("\nInserta el Piso Base: ")
                            pisob = listaPisos.busquedaPiso(pisoBase)
                            if pisob == None:
                                print(Fore.RED,"No Existe el Piso Error!")
                            else:
                                print("Piso: ", pisob.piso, " Filas: ", pisob.fila, " Columna: ",pisob.columna)
                                print(Fore.LIGHTCYAN_EX,"El Piso fue encontrado con Exito!!!!!\n")
                                pisob.listaPatron.sortPatron()
                                pisob.listaPatron.recorrerPatron()

                                codigoBase = input("\nInserta el Codigo a Graficar: ")
                                codigob = pisob.listaPatron.busquedaPatron(codigoBase)
                                if codigob == None:
                                    print(Fore.RED, "No Existe el Codigo Error!")
                                else:
                                    print(Fore.LIGHTMAGENTA_EX, "\nEl Patron a Trabajar es: \n")
                                    print(Fore.LIGHTGREEN_EX, "Codigo: ", codigob.codigo)
                                    print(Fore.LIGHTGREEN_EX, "Patron: ", codigob.patron,"\n")
                                    print(Fore.LIGHTYELLOW_EX, "Se almaceno la Infomacion del Piso Base con Exito!!!!\n")
                                    lista_pisob = pisob.listaPatron.busquedaPatron(codigoBase).listaCodigos
                                    grafica.graphic(pisoBase, pisob.fila, pisob.columna, codigoBase, lista_pisob)


                            print(Fore.LIGHTGREEN_EX, "Listado de Pisos A-Z")
                            listaPisos.bubbleSortPisos()
                            listaPisos.recorrerPiso()

                            pisoCambio = input("\nInserta el Piso Cambio: ")
                            pisoc = listaPisos.busquedaPiso(pisoCambio)
                            if pisoc == None:
                                print(Fore.RED,"No Existe el Piso Error!")
                            else:
                                if pisoCambio == pisoBase:
                                    print("Piso: ", pisoc.piso, " Filas: ", pisoc.fila, " Columna: ",pisoc.columna)
                                    print(Fore.LIGHTCYAN_EX,"El Piso fue encontrado con Exito!!!!!\n")
                                    pisoc.listaPatron.sortPatron()
                                    pisoc.listaPatron.recorrerPatron()

                                    codigoCambio = input("\nInserta el Codigo a Graficar: ")
                                    codigoc = pisoc.listaPatron.busquedaPatron(codigoCambio)
                                    if codigoc == None:
                                        print(Fore.RED, "No Existe el Codigo Error!")
                                    else:
                                        print(Fore.LIGHTMAGENTA_EX, "\nEl Patron a Trabajar es: \n")
                                        print(Fore.LIGHTGREEN_EX, "Codigo: ", codigoc.codigo)
                                        print(Fore.LIGHTGREEN_EX, "Patron: ", codigoc.patron,"\n")
                                        print(Fore.LIGHTYELLOW_EX, "Se almaceno la Infomacion del Piso Cambio con Exito!!!!\n")
                                        lista_pisoc = pisoc.listaPatron.busquedaPatron(codigoCambio).listaCodigos
                                        #grafica.graphic(pisoCambio, pisoc.fila, pisoc.columna, codigoCambio, lista_pisoc)
                                        matriz.matrix(pisoBase,codigoBase,codigob.patron,int(pisob.volteo),int(pisob.intercambiar), pisob.fila, pisob.columna, lista_pisob, lista_pisoc)
                                        #matriz.algoritmo(pisoBase, codigoBase,codigob.patron,int(pisob.volteo), int(pisob.intercambiar),pisob.fila, pisob.columna, lista_pisob, lista_pisoc)
                                        print("Generando Cambios Espere")


                                else:
                                    print(Fore.RED,"\nSolo puedo hacer cambios en el mismo Piso!!!\n")

                elif opcionMenu == self.imprimir:
                    opcN = ''

                    while opcN != '0':
                        print(Fore.BLUE, "Impresion Orden\n")
                        print(Fore.BLUE, "1) -> Imprimir en Consola")
                        print(Fore.BLUE, "2) -> Generar archivo .txt")
                        print(Fore.BLUE, "0) -> Salir")

                        opcN = input("\nIngresa Opción: ")

                        if opcN == '1':
                            secuencia = matriz.retornoCadena()
                            print(Fore.LIGHTWHITE_EX,secuencia)
                        elif opcN == '2':
                            img = "C:\\Users\\santi\\PyCharmProyect\\IPC2\\Proyecto_1\\app\\Graphics\\Instrucciones.txt"
                            os.startfile(img)

                elif opcionMenu == self.salir:
                    print("\nEsto no es un adios sino un asta pronto!!!!!!\n")
                    False
                    break
                else:
                    print(Fore.YELLOW,'Opcion no válida...')
                input('\nPresiona enter para Ingresar al Menú...')

            except ValueError as error:
                opcionMenu = -1
                print(Fore.RED,f'Error: {error}')
                print(Fore.RED,'El programa no permite carateres tipo Caracter')
                input('Presione la tecla para continuar@')




    def readXML(self,nuevaRuta):
        tree = ET.parse(nuevaRuta)
        root = tree.getroot()
        listaPisos = PisoListaSimple()

        for pisos in root:
            for filas in pisos.iter('R'):
                fila = filas.text.strip()
            for columnas in pisos.iter('C'):
                columna = columnas.text.strip()
            for volteos in pisos.iter('F'):
                volteo = volteos.text.strip()
            for intercambios in pisos.iter('S'):
                intercambio = intercambios.text.strip()
            nuevoPiso = Piso(pisos.attrib['nombre'],fila,columna,volteo,intercambio)
            listaPisos.append(nuevoPiso)
            for patrones in pisos.iter('patron'):
                nuevoPatron = Patron(patrones.attrib['codigo'],patrones.text)
                nuevoPiso.listaPatron.append(nuevoPatron)

                letras = patrones.text.strip()
                letra = str(letras)
                cont = 0
                for f in range(1,int(fila)+1):
                    for c in range(1,int(columna)+1):
                        l = letra[cont]
                        nuevoCodigo = Codigo(l, f, c)
                        nuevoPatron.listaCodigos.append(nuevoCodigo)
                        cont = cont + 1

        return listaPisos



