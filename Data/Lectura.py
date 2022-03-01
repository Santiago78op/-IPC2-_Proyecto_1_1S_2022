
class Analizador():

    def Leer(self, extension):
        contenido = ""
        direccion = extension.replace("//", "/")
        with open(direccion,'r') as file:
            for linea in file:
                contenido += linea.strip()
        file.close()
        return contenido


    def guardar(self,contenido):
        nueva_ruta = "C:/Users/santi/PyCharmProyect/IPC2/Proyecto_1/app/Directorios/archivo.xml"
        archivo = open(f"{nueva_ruta}", 'w')
        archivo.write(contenido)
        return nueva_ruta













