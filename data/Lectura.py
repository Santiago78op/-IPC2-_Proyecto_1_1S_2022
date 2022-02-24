from xml.dom.minidom import parse

class Analizador:

    def __init__(self):
        self.titulo = ""

    def Leer(self, extension):
        contenido = ""
        direccion = extension.replace("//", "/")
        with open(direccion,'r') as file:
            for linea in file:
                contenido += linea
        file.close()
        self.guardar(contenido)

    def guardar(self,contenido):
        nueva_ruta = "C:/Users/santi/PyCharmProyect/IPC2/Proyecto_1/app/Directorios/archivo.xml"
        archivo = open(f"{nueva_ruta}", 'w')
        archivo.write(contenido)


    def readXML(self):
        domTree = parse("C:/Users/santi/PyCharmProyect/IPC2/Proyecto_1/app/Directorios/archivo.xml")
        rootNode = domTree.documentElement
        print(rootNode.nodeName)
        self.titulo = rootNode.nodeName
        pisos = rootNode.getElementsByTagName("piso")
        for piso in pisos:
            if piso.hasAttribute("nombre"):
                print("Piso:", piso.getAttribute("nombre"))
                R = piso.getElementsByTagName("R")[0]
                print(R.nodeName, ":", R.childNodes[0].data)
                C = piso.getElementsByTagName("C")[0]
                print(C.nodeName, ":", C.childNodes[0].data)
                F = piso.getElementsByTagName("F")[0]
                print(F.nodeName, ":", F.childNodes[0].data)
                S = piso.getElementsByTagName("S")[0]
                print(S.nodeName, ":", S.childNodes[0].data)
                patrones = piso.getElementsByTagName("patron")
                for patron in patrones:
                    if patron.hasAttribute("codigo"):
                        print("Codigo:", patron.getAttribute("codigo"))
                        print("Patron:", patron.firstChild.data)







