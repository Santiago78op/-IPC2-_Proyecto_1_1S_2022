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
            label= "PATRON" 
            bgcolor = "green"
            raiz[label =''' + nombreCod + ''']
            edge[dir = "both"]
        '''
        for i in range(1, int(filas) + 1):
            diagrama = (diagrama+'''
            Fila'''+str(i)+'''[label=" '''+str(i)+'''",group='''+str(1)+'''];''')
        '''
        '''
        for ii in range(1, int(filas)):
            '''Fila'''+str(ii)+'''->''''''Fila'''+str(ii + 1)+''';'''
        '''
        '''
        for w in range(1, int(columnas) + 1):
            '''Columna'''+str(w)+'''[label="'''+str(w)+'''",group='''+str(w + 1)+'''];'''
        '''
        '''
        for z in range(1, int(columnas)):
            '''Columna'''+str(z)+'''->''''''Columna'''+str(z + 1)+''';'''
        '''
        
        raiz->Fila1;
        raiz->Columna1;
        
        '''
        cadena = ""
        for y in range(1, int(columnas) + 1):
            cadena += '''Columna'''+str(y)+''';'''
        ''''{rank = same;raiz;'''+cadena+'''}"'''
        '''
        
        }
        }
        '''

        ruta = 'Graphics\\imagen.txt '
        file = open(ruta, 'w')
        file.write(f"{diagrama}")
        file.close()
        #ver = "dot -Tpng C:\\Users\\santi\\PyCharmProyect\\IPC2\\Proyecto_1\\app\\Graphics\\imagen.txt -o C:\\Users\\santi\\PyCharmProyect\\IPC2\\Proyecto_1\\app\\Graphics\\grafica.png"
        #status = os.system(ver)
        #img = "C:\\Users\\santi\\PyCharmProyect\\IPC2\\Proyecto_1\\app\\Graphics\\grafica.png"
        #stado = os.startfile(img)

        #   subgraph cluster_p{
        # label= "PISO ''' + str(nombrePiso) + ''' " 
        # label= "PATRON"
        # bgcolor = "skyblue"
        # raiz[label =''' + nombreCod + ''']
        #  edge[dir = "both"]
        #graphviz = graphviz + '''
        #          bgcolor = "skyblue"
        #          raiz[label =''' + nombreCod + ''']
        #          edge[dir = "both"]
        #          --#quitar comentario--
        #          /*Aqui creamos las cabeceras
        #          de las filas*/'''

        #for i in range(1, int(filas) + 1):
        #     graphviz = graphviz + '''
        #              Fila''' + str(i) + '''[label=" ''' + str(i) + '''",group=''' + str(1) + '''];'''

        # for j in range(1, int(filas)):
        #     graphviz = graphviz + '''
        #          Fila''' + str(j) + '''->Fila''' + str(j + 1) + '''
        #              '''

        # for w in range(1, int(columnas) + 1):
        #     graphviz = graphviz + '''
        #              Columna''' + str(w) + '''[label=" ''' + str(w) + '''",group=''' + str(w + 1) + '''];'''

        # for z in range(1, int(columnas)):
        #     graphviz = graphviz + '''
        #          Columna''' + str(z) + '''->Columna''' + str(j + 1) + '''
        #              '''

        # graphviz = graphviz + '''
        #          raiz->Fila_1;
        #          raiz->Columna_1;
        #          '''
        # # {rank = same;
        # # raiz;
        # # Columna1;
        # # Columna2;
        # # Columna3;
        # # Columna4;
        # # Columna5;}

        # cadena = ""
        # for y in range(1, int(columnas) + 1):
        #     cadena += "Columna" + str(y) + ";"
        # graphviz = graphviz + '''
        #      {
        #      '''
        # graphviz = graphviz + '''
        #      rank=same;raiz;''' + cadena + "}"'''
        #      '''

        # for f in range(1, int(filas) + 1):
        #     for c in range(1, int(columnas) + 1):
        #         graphviz = graphviz + '''
        #                  nodo''' + str(f) + '''_''' + str(c) + '''[label=" ''' + str(
        #             letras.buscarLetra(f,c)) + ''' ",fillcolor=orange,group=''' + str(c + 1) + '''];'''

        # for ff in range(1, int(filas) + 1):
        #     graphviz = graphviz + '''
        #          Fila''' + str(ff) + '''->nodo''' + str(ff) + '''_''' + str(1) + ''';
        #          {
        #           '''

        #     cade = ""
        #     for o in range(1, int(columnas) + 1):
        #         cade += ";nodo" + str(ff) + "_" + str(o)
        #     graphviz = graphviz + '''
        #          rank=same;Fila''' + str(ff) + cade + '''
        #          }
        #          '''

        #     for t in range(1, int(columnas) + 1):
        #         graphviz = graphviz + '''
        #              Columna''' + str(t) + '''->nodo''' + str(1) + '''_''' + str(t) + ''';
        #               '''

        #     for l in range(1, int(filas) + 1):
        #         for c in range(1, int(columnas)):
        #             graphviz = graphviz + '''
        #                  nodo''' + str(l) + '''''' + str(c) + '''->nodo''' + str(l) + '''''' + str(c + 1) + ''';
        #                  '''

        #     for l in range(1, int(filas)):
        #         for c in range(1, int(columnas) + 1):
        #             graphviz = graphviz + '''
        #                  nodo''' + str(l) + '''''' + str(c) + '''->nodo''' + str(l + 1) + '''''' + str(c) + ''';
        #                  '''
        #     graphviz = graphviz + '''
        #              }
        #              }
        # 
        # '''


