from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

class GUI:

    def __init__(self) -> None:
        raiz = Tk()
        raiz.title("Change Floor")
        raiz.geometry("835x450")
        raiz.rowconfigure(0, weight=1)
        raiz.columnconfigure(0, weight=1)

        mainframe = ttk.Frame(raiz)
        mainframe.grid(row=0, column=0, sticky=NSEW)
        mainframe.columnconfigure(1, weight=1)
        mainframe.columnconfigure(2, weight=2)
        mainframe.rowconfigure(1, weight=1)

        #contenedor botones
        panel_1 = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
        panel_1.grid(row=1, column=1, sticky=NSEW)
        panel_1.columnconfigure(1, weight=1)
        panel_1.columnconfigure(2, weight=1)
        panel_1.columnconfigure(3, weight=1)
        panel_1.rowconfigure(1, weight=1)
        panel_1.rowconfigure(2, weight=1)
        panel_1.rowconfigure(3, weight=1)
        panel_1.rowconfigure(4, weight=1)
        panel_1.rowconfigure(5, weight=1)
        panel_1.rowconfigure(6, weight=1)
        panel_1.rowconfigure(7, weight=1)
        panel_1.rowconfigure(8, weight=1)
        panel_1.rowconfigure(9, weight=1)
        panel_1.rowconfigure(10, weight=1)
        panel_1.rowconfigure(11, weight=1)

        Cargar_Archivo = ttk.Label(panel_1,text="Cargar Archivo .XML")
        Cargar_Archivo.grid(row=1, column=2, sticky=EW)

        Button_Cargar = ttk.Button(panel_1,text="Cargar Archivo .XML")
        Button_Cargar.grid(row=2, column=2, sticky=EW)

        Graficar_Patron = ttk.Label(panel_1, text="Graficar Patron")
        Graficar_Patron.grid(row=3, column=2, sticky=EW)

        Piso = ttk.Label(panel_1, text="Piso")
        Piso.grid(row=4, column=1, sticky=EW)

        niveles = ["Piso1", "Piso2","Piso3","Piso4"]
        combox_Pisos = ttk.Combobox(panel_1, values=niveles)
        combox_Pisos.grid(row=4, column=2, sticky=EW)

        Patron = ttk.Label(panel_1, text="Patron")
        Patron.grid(row=5, column=1, sticky=EW)

        patrones = ["Piso1", "Piso2","Piso3","Piso4"]
        combox_Patron = ttk.Combobox(panel_1, values=patrones)
        combox_Patron.grid(row=5, column=2, sticky=EW)

        Button_Graficar = ttk.Button(panel_1,text="Graficar")
        Button_Graficar.grid(row=6, column=2, sticky=EW)

        Patron = ttk.Label(panel_1, text="Patron")
        Patron.grid(row=5, column=1, sticky=EW)

        Operacion = ttk.Label(panel_1, text="Operaciones")
        Operacion.grid(row=7, column=2, sticky=EW)

        Piso_Nuevo = ttk.Label(panel_1, text="Piso")
        Piso_Nuevo.grid(row=8, column=1, sticky=EW)
        patrones_1 = ["Piso1", "Piso2","Piso3","Piso4"]
        combox_Cambio_Piso = ttk.Combobox(panel_1, values=patrones_1)
        combox_Cambio_Piso.grid(row=8, column=2, sticky=EW)

        Patron_Nuevo = ttk.Label(panel_1, text="Patron")
        Patron_Nuevo.grid(row=9, column=1, sticky=EW)
        patrones_2 = ["Piso1", "Piso2","Piso3","Piso4"]
        combox_Cambio_Patron = ttk.Combobox(panel_1, values=patrones_2)
        combox_Cambio_Patron.grid(row=9, column=2, sticky=EW)

        Cambiar_Patron = ttk.Label(panel_1, text="Cambiar Patron")
        Cambiar_Patron.grid(row=10, column=1, sticky=EW)
        patrones_3 = ["Piso1", "Piso2","Piso3","Piso4"]
        combox_Nuevo_Cambio_Patron = ttk.Combobox(panel_1, values=patrones_3)
        combox_Nuevo_Cambio_Patron.grid(row=10, column=2, sticky=EW)

        Button_Cambiar = ttk.Button(panel_1,text="Cambiar")
        Button_Cambiar.grid(row=11, column=2, sticky=EW)

        #Container
        panel_2 = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
        panel_2.grid(row=1, column=2, sticky=NSEW)
        panel_2.columnconfigure(1, weight=1)
        panel_2.rowconfigure(2, weight=1)

        Pisos_en_Archivo = ttk.Label(panel_2, text="Contenido Documento en Orden")
        Pisos_en_Archivo.grid(row=1, column=1, sticky=NSEW)

        contenido = Listbox(panel_2)
        contenido.grid(row=2, column=1, sticky=NSEW)

        raiz.mainloop()