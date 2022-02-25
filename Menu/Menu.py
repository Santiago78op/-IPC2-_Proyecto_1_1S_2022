import os
from Data.Lectura import Analizador
from Data.CreacionAtributos import Atributos

class Menu:

    def __init__(self):
        self.cargar = "a"
        self.mostrar_conte = "b"
        self.graficar_patron = "c"
        self.cambiar_patron = "d"
        self.salir = "z"

    def mostrar_menu(self) -> None:
        """
        Función que limpia la pantalla y muestra nuevamente el menu
        """
        os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
        print(f'''\t<--Menu Principal-->\n
Selecciona una opción:\n
    \t{self.cargar }) - Cargar Archivo .XML
    \t{self.mostrar_conte}) - Mostrar Contenido
    \t{self.graficar_patron}) - Graficar Patron
    \t{self.cambiar_patron}) - Cambiar Patron
    \t{self.salir}) - Salir\n''')

    def menu(self) -> bool:
        infodata = Analizador()
        atri = Atributos()
        #cargar_imagen = analizar_Imagen.Analizarimagen()

        while True:

            self.mostrar_menu()

            opcionMenu = input("Inserta el numero de la opcion: >> ")

            try:
                opcionMenu = str(opcionMenu)
            except ValueError as error:
                opcionMenu = -1
                print(f'Error: {error}')
                print('El programa no permite carateres tipo Digito')
                input('Presione la tecla para continuar@')

            os.system('cls')

            if opcionMenu == self.cargar:
                carga = input("Inserta la ruta del archivo .xml: >> \n")
                infodata.Leer(carga)
                infodata.readXML()
            elif opcionMenu == self.mostrar_conte:
                titulo = infodata.procesar_titulo()
                piso = infodata.procesar_piso()
                atri.redesign(titulo,piso)
            elif opcionMenu == self.graficar_patron:
                print("Graficar Patron")
            elif opcionMenu == self.cambiar_patron:
                print("Cambiar Patron")
            elif opcionMenu == self.salir:
                print("Esto no es un adios sino un asta pronto\n")
                False
                break
            else:
                print('Opcion no válida...')
            input('Presiona enter para Ingresar al Menú...')







