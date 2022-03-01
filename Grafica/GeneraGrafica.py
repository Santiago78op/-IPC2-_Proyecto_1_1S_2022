from Lista.ListaCodDoble import ListaCodDoble
from os import system,startfile

class Grafica():

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