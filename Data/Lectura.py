from xml.dom.minidom import parse


class Analizador:

    def __init__(self):
        self.titulo = ""
        self.piso = ""

    def Leer(self, extension):
        contenido = ""
        direccion = extension.replace("//", "/")
        with open(direccion,'r') as file:
            for linea in file:
                contenido += linea.strip()
        file.close()
        self.guardar(contenido)

    def guardar(self,contenido):
        nueva_ruta = "C:/Users/santi/PyCharmProyect/IPC2/Proyecto_1/app/Directorios/archivo.xml"
        archivo = open(f"{nueva_ruta}", 'w')
        archivo.write(contenido)


    def readXML(self):
        contenedor = []
        contador_pisos = 0
        domTree = parse("C:/Users/santi/PyCharmProyect/IPC2/Proyecto_1/app/Directorios/archivo.xml")
        rootNode = domTree.documentElement
        titulo = rootNode.nodeName
        pisos = rootNode.getElementsByTagName("piso")
        for piso in pisos:
            if piso.hasAttribute("nombre"):
                numero_piso = piso.getAttribute("nombre")
                #print("Piso:", piso.getAttribute("nombre"))
                R = piso.getElementsByTagName("R")[0]
                columna = R.childNodes[0].data
                #print(R.nodeName, ":", R.childNodes[0].data)
                C = piso.getElementsByTagName("C")[0]
                celda = C.childNodes[0].data
                #print(C.nodeName, ":", C.childNodes[0].data)
                F = piso.getElementsByTagName("F")[0]
                volteo = F.childNodes[0].data
                #print(F.nodeName, ":", F.childNodes[0].data)
                S = piso.getElementsByTagName("S")[0]
                intercambio = S.childNodes[0].data
                #print(S.nodeName, ":", S.childNodes[0].data)
                contenedor.append([numero_piso, columna, celda, volteo, intercambio])
                contador_pisos = contador_pisos
                patrones = piso.getElementsByTagName("patron")
                for patron in patrones:
                    if patron.hasAttribute("codigo"):
                        #print("Codigo:", patron.getAttribute("codigo"))
                        #print("Patron:", patron.firstChild.data)
                        codigo = patron.getAttribute("codigo")
                        num_patron = patron.firstChild.data
                        #contenedor[contador_pisos][len(contenedor[contador_pisos]):] = [[codigo,num_patron]]
                        contenedor[contador_pisos].append([codigo,num_patron])
                contador_pisos = contador_pisos + 1

        self.titulo = titulo
        self.piso = contenedor


    def procesar_titulo(self):
        return self.titulo

    def procesar_piso(self):
        return self.piso



