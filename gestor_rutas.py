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

# Función para encontrar las rutas más cortas utilizando Dijkstra
def encontrar_rutas(grafo, inicio):
    rutas = nx.single_source_dijkstra_path(grafo, inicio)
    costos = nx.single_source_dijkstra_path_length(grafo, inicio)
    for destino, ruta in rutas.items():
        if destino != inicio:
            costo_total = costos[destino]
            print(f"Desde {inicio} hasta {destino}: {ruta}, Costo total: {costo_total}")