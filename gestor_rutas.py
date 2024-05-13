import networkx as nx

# Función para leer el archivo y crear el grafo
def crear_grafo():
    grafo = nx.Graph()
    with open('rutas.txt', 'r') as file:
        for linea in file:
            inicio, fin, costo = linea.strip().split(',')
            costo = int(costo)
            grafo.add_edge(inicio.strip(), fin.strip(), weight=costo)
    return grafo
