

class Analizador:


    def Leer(self, extension):
        contenido = ""
        extension.replace("//","/")
        with open(f"{extension}",'r') as file:
            for linea in file:
                contenido += linea
        file.close()
        self.guardar(contenido)

    def guardar(self,contenido):
        nueva_ruta = "C:/Users/santi/PyCharmProyect/IPC2/Proyecto_1/app/Directorios/archivo.xml"
        archivo = open(f"{nueva_ruta}", 'w')
        archivo.write(contenido)

