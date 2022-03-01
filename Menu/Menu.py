import os
from os import system,startfile
from colorama import Fore
from Data.Lectura import Analizador
from Constructor.Patron import Patron
from Constructor.Piso import Piso
from Constructor.Codigo import Codigo
from Lista.ListaSimple import PisoListaSimple
from Lista.ListaCodDoble import ListaCodDoble
import xml.etree.ElementTree as ET


class Menu():

    def __init__(self):
        self.cargar = 1
        self.graficar_patron = 2
        self.cambiar_patron = 3
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
    \t{self.salir}) - Salir\n''')

    def menu(self) -> bool:
        infodata = Analizador()
        listaPisos = PisoListaSimple()


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
                            listaPisos.sortSimpleListPisos()
                            listaPisos.printSimplePiso()
                            nombrePiso = input("Inserta el Piso: ")
                            piso = listaPisos.buscarPiso(nombrePiso)
                            if piso == None:
                                print(Fore.RED,"No Existe el Piso Error!")
                            else:
                                print(Fore.LIGHTGREEN_EX,"Piso: ",piso.piso)
                                piso.listaPatron.sortDoubleListPatron()
                                piso.listaPatron.printDoblePatron()

                            nombreCodigo = input("Inserta el Codigo a Graficar: ")
                            codigo = piso.listaPatron.buscarPatron(nombreCodigo)
                            if codigo == None:
                                print(Fore.RED, "No Existe el Codigo Error!")
                            else:
                                print(Fore.LIGHTMAGENTA_EX, "\nEl Patron a Trabajar es: \n")
                                print(Fore.LIGHTGREEN_EX, "Codigo: ", codigo.codigo)
                                print(Fore.LIGHTGREEN_EX, "Patron: ", codigo.patron,"\n")
                                codigo.listaCodigos.printDobleCod()


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
                            listaPisos.sortSimpleListPisos()
                            listaPisos.printSimplePiso()
                            nombrePiso = input("Inserta el Piso: ")
                            piso = listaPisos.buscarPiso(nombrePiso)
                            if piso == None:
                                print(Fore.RED,"No Existe el Piso Error!")
                            else:
                                print(Fore.LIGHTGREEN_EX,"Piso: ",piso.piso)
                                piso.listaPatron.sortDoubleListPatron()
                                piso.listaPatron.printDoblePatron()
                                nombreCodigo = input("\nInserta el Codigo a Base: ")
                                codigo = piso.listaPatron.buscarPatron(nombreCodigo)
                                if codigo == None:
                                    print(Fore.RED, "No Existe el Codigo Error!")
                                else:
                                    print(Fore.LIGHTMAGENTA_EX, "\nEl Patron Base: \n")
                                    print(Fore.LIGHTGREEN_EX, "Codigo: ", codigo.codigo)
                                    print(Fore.LIGHTGREEN_EX, "Patron: ", codigo.patron,"\n")

                                nombreCodigoCambio = input("Inserta el Codigo a Cambiar: ")
                                codigoCambio = piso.listaPatron.buscarPatron(nombreCodigoCambio)
                                if codigoCambio == None:
                                    print(Fore.RED, "No Existe el Codigo Error!")
                                else:
                                    print(Fore.LIGHTMAGENTA_EX, "\nEl Patron al cual se Cambiara Patron Base: \n")
                                    print(Fore.LIGHTGREEN_EX, "Codigo: ", codigoCambio.codigo)
                                    print(Fore.LIGHTGREEN_EX, "Patron: ", codigoCambio.patron, "\n")
                                    print(Fore.LIGHTMAGENTA_EX, "\nGraficandooooo.....!!!!!! \n")

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
                fila = filas.text
            for columnas in pisos.iter('C'):
                columna = columnas.text
            for volteos in pisos.iter('F'):
                volteo = volteos.text
            for intercambios in pisos.iter('S'):
                intercambio = intercambios.text
            nuevoPiso = Piso(pisos.attrib['nombre'],fila,columna,volteo,intercambio)
            listaPisos.append(nuevoPiso)
            for patrones in pisos.iter('patron'):
                letra = patrones.text
                nuevoPatron = Patron(patrones.attrib['codigo'],patrones.text)

                cont = 0
                for f in range(1,int(fila)+1):
                    for c in range(1,int(columna)+1):
                        l = letra[cont]
                        nuevoCodigo = Codigo(f, c, l)
                        nuevoPatron.listaCodigos.append(nuevoCodigo)
                        cont = cont + 1

                nuevoPiso.listaPatron.append(nuevoPatron)

        return listaPisos



    def graphic(self, nombrePiso,filas,columnas,nombreCod,letras=ListaCodDoble()):
        graphviz = ''' 
                   digraph S{
        node[shape=box fillcolor="white" style =filled]
        subgraph cluster_p{
        label= "PISO '''+nombrePiso+''' " 
        label= "PATRON "
        '''

        graphviz = graphviz + '''
                bgcolor = "skyblue"
                raiz[label =''' + nombreCod + ''']
                edge[dir = "both"]
                --#quitar comentario--
                /*Aqui creamos las cabeceras
                de las filas*/'''

        for i in range(1,int(filas)+1):
            graphviz = graphviz + '''
                    Fila'''+str(i)+'''[label=" ''' +str(i)+'''",group='''+str(1)+'''];'''

        for j in range(1, int(filas)):
            graphviz = graphviz + '''
                Fila''' + str(j) + '''->Fila''' + str(j + 1) + '''
                    '''

        for w in range(1,int(columnas)+1):
            graphviz = graphviz + '''
                    Columna'''+str(w)+'''[label=" ''' +str(w)+'''",group='''+str(w+1)+'''];'''

        for z in range(1, int(columnas)):
            graphviz = graphviz + '''
                Columna''' + str(z) + '''->Columna''' + str(j + 1) + '''
                    '''

        graphviz=graphviz+'''
                raiz->Fila1;
                raiz->Columna1;
                '''