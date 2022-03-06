from Lista.ListaCodDoble import ListaCodDoble
from os import system,startfile

import  os

class Grafica():

    def graphic(self,nombrePiso, filas, columnas, nombreCod, letras = ListaCodDoble()):
        diagrama ='''
        digraph S{
            node[shape=box fillcolor="white" style =filled]
            
            subgraph cluster_p{
            label = "PISO: '''+ nombrePiso +'''"
            bgcolor = "green"
            raiz[label =''' + nombreCod + ''']
            edge[dir = "both"]
        '''
        for i in range(1, int(filas) + 1):
            diagrama = (diagrama+'''
            Fila'''+str(i)+'''[label=" '''+str(i)+'''",group='''+str(1)+'''];''')

        for ii in range(1, int(filas)):
            diagrama = (diagrama+'''
            Fila'''+str(ii)+'''->Fila'''+str(ii + 1)+''';''')

        for w in range(1, int(columnas) + 1):
            diagrama = (diagrama+'''
            Columna'''+str(w)+'''[label="'''+str(w)+'''",group='''+str(w + 1)+''',fillcolor=yellow];''')

        for z in range(1, int(columnas)):
            diagrama = (diagrama+'''
            Columna'''+str(z)+'''->Columna'''+str(z + 1)+''';''')

        diagrama = (diagrama+'''
            raiz->Fila1;
            raiz->Columna1;
            ''')

        cadena = ""
        pc = ";"
        for y in range(1, int(columnas) + 1):
            cadena +='''Columna'''+str(y)+pc


        diagrama = (diagrama+'''
        {rank = same;raiz;'''+cadena[:-1]+'''}
        ''')

        for f in range(1, int(filas) + 1):
            for c in range(1, int(columnas) + 1):
                diagrama = (diagrama+'''
            nodo'''+str(f)+'''_'''+str(c)+'''[label=" '''+str(
            letras.buscarLetra(f,c))+'''",fillcolor=orange,group='''+str(c + 1)+'''];''')

        for ff in range(1, int(filas) + 1):
            diagrama = (diagrama + '''
            Fila'''+str(ff)+'''->nodo'''+str(ff)+'''_'''+str(1)+''';
            {
            ''')
            cadena_1 = ""
            for o in range(1, int(columnas) + 1):
                cadena_1 += ";nodo"+str(ff)+"_"+str(o)
            diagrama = (diagrama+'''
                rank=same;Fila'''+str(ff)+cadena_1+'''}
                ''')

        for t in range(1, int(columnas) + 1):
            diagrama = (diagrama+'''
            Columna'''+str(t)+'''->nodo'''+str(1)+'''_'''+str(t)+''';
            ''')

        for l in range(1, int(filas) + 1):
            for c in range(1, int(columnas)):
                diagrama = (diagrama+'''
            nodo'''+str(l)+'''_'''+str(c)+'''->nodo'''+str(l)+'''_'''+str(c + 1)+''';
            ''')

        for l in range(1, int(filas)):
            for c in range(1, int(columnas) + 1):
                diagrama = diagrama + '''
                    nodo''' + str(l) + '''_''' + str(c) + '''->nodo''' + str(l + 1) + '''_''' + str(c) + ''';
                    '''

        diagrama = (diagrama+'''
            }
        }
        ''')


        ruta = 'Graphics\\imagen.txt '
        file = open(ruta, 'w')
        file.write(f"{diagrama}")
        file.close()
        ver = "dot -Tpng C:\\Users\\santi\\PyCharmProyect\\IPC2\\Proyecto_1\\app\\Graphics\\imagen.txt -o C:\\Users\\santi\\PyCharmProyect\\IPC2\\Proyecto_1\\app\\Graphics\\grafica.png"
        status = os.system(ver)
        img = "C:\\Users\\santi\\PyCharmProyect\\IPC2\\Proyecto_1\\app\\Graphics\\grafica.png"
        stado = os.startfile(img)