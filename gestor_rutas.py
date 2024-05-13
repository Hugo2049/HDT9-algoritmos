import networkx as nx

# Función para leer el archivo y crear el grafo
def crear_grafo(ruta_archivo):
    grafo = nx.Graph()
    with open(ruta_archivo, 'r') as file:
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

# Función para mostrar las posibles destinos desde una estación de salida
def mostrar_destinos(grafo, inicio):
    destinos = list(grafo.neighbors(inicio))
    print(f"Posibles destinos desde {inicio}: {destinos}")

# Función principal
def main():
    ruta_archivo = "C:/Users/Usuario/Documents/GitHub/Radio/HDT9-algoritmos/rutas.txt"
    grafo = crear_grafo(ruta_archivo)
    print("Grafo cargado:")
    print(grafo.nodes())  # Imprimir las estaciones en el grafo
    print()
    while True:
        inicio = input("Ingrese la estación de salida (o 'salir' para terminar): ").strip()
        if inicio.lower() == 'salir':
            break
        if inicio not in grafo:
            print("Estación no encontrada. Por favor, ingrese una estación válida.")
            continue
        mostrar_destinos(grafo, inicio)
        encontrar_rutas(grafo, inicio)

if __name__ == "__main__":
    main()
