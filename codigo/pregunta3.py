import pdb

'''
CODIGO DE bellman_ford MODIFICADO PARA MOSTRAR CADA TABLA EN CADA ITERACION PARA CADA ROUTER Y ADEMAS 
QUE PUEDA RECORRER LOS DICCIONARIOS GENERADOS PARA IMPRIMIR EN PANTALLA LAS TABLAS.

CONSIDERAR p como PC y s como Servidor

EL CODIGO IMPRIME TABLAS DE MAS (SE REPITEN), ESTO ES PORQUE SE DEMORA ALGUNAS ITERACIONES EN COMPROBAR LA CONVERGENCIA 
Y ASI CONSIDERAR EL RESULTADO COMO RUTA MINIMA.

ESTE CODIGO CORRESPONDE A LA PREGUNTA 3, DONDE SE MODIFICO EL GRAFO ORIGINAL, ELIMINANDO LA CONEXION EXISTENTE ENTRE LOS NODOS H e I.
'''

# Para cada nodo se selecciona el destinatario y el nodo que lo precede
def initialize(grafo, origen):
    d = {} # nodo destinatario
    p = {} # nodo que precede
    for nodo in grafo:
        d[nodo] = float('Inf') # Asignamos infinito, asumiendo que los nodos estan lejos o son inalcazables.
        p[nodo] = None
    d[origen] = 0 # Asignamos 0 al nodo origen
    return d, p

def relax(nodo, vecino, grafo, d, p):
    #Se recorre el diccionario que tiene el nodo y el costo del nodo desde cada router y se imprime de la manera mas ordenada que pude.
    #if (nodo == 'p'):    
    print "tabla de "+nodo
    nodos = d.keys()
    valores = d.values()
    elementos = d.items()
    count = 0;

    print "nodo: ",
    for n,v in elementos:
        print n,
        print "      ",
    print ""
    print "costo:",
    for n,v in elementos:
        print v,
        if count == 0:
            print "  ",
            count=count+1
        else:
            print "      ",
    print "\n"
        
        
        
    #print "vecino: "+vecino
    #print d[vecino]
    #si la distancia entre el nodo y el vecino es menos que la que ya tengo asignada, se reemplaza por la nueva distancia menor
    if d[vecino] > d[nodo] + grafo[nodo][vecino]:
        # Aqui se guarda la nueva distancia
        d[vecino]  = d[nodo] + grafo[nodo][vecino]
        p[vecino] = nodo

#algoritmo de ruta minia (bellman ford) para recorrer el grafo
def bellman_ford(grafo, origen):
    d, p = initialize(grafo, origen)
    for i in range(len(grafo)-1): #se ejecuta el codigo hasta que los resultados converjan, esto nos indica que llegamos a la ruta minima
        for u in grafo:
            for v in grafo[u]: #para cada vecino de u
                relax(u, v, grafo, d, p) #calculamos el costo


    # Finalmente se revisa si exiten ciclos de peso negativo
    for u in grafo:
        for v in grafo[u]:
            assert d[v] <= d[u] + grafo[u][v]

    return d, p


def tarea3_pregunta3():
    #GRAFO MODIFICADO ELIMIMANDO LA CONEXION H e I
    grafo = {
        'p': {'a': 3},
        'a': {'p': 3, 'b': 1, 'g': 4, 'i':  10},
        'b': {'a': 1, 'c': 9, 'e': 8},
        'c': {'b': 9, 'd': 2},
        'd': {'c': 9, 'f': 9, 'e': 9, 'i': 2},
        'e': {'f': 2, 'i': 1, 'd': 2, 'b': 9},
        'f': {'d': 9,'e': 2,'h': 6},
        'g': {'a': 4, 'h': 7},
        'h': {'g': 7, 'f': 6},
        'i': {'a': 10, 'd': 2, 'e': 1, 's': 1},
        's': {'i': 1}
        }

    d, p = bellman_ford(grafo, 'p')

    #Se recorre el diccionario final que contiene la ruta minima hacia cada nodo desde PC, y se imprime en pantalla
    print "ruta minima desde PC hacia -->"

    elementos = d.items()

    print "nodo: ",
    for n,v in elementos:
        print n,
        print "      ",
    print ""
    print "costo:",
    for n,v in elementos:
        print v,
        print "      ",
    print "\n"

if __name__ == '__main__': tarea3_pregunta3()