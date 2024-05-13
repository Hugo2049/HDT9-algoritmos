# Importamos las librerías necesarias
import networkx as nx
import matplotlib.pyplot as plt

# Función para leer el archivo y crear el grafo
def crear_grafo(ruta_archivo):
    # Creamos un grafo vacío
    grafo = nx.Graph()
    # Abrimos el archivo de rutas
    with open(ruta_archivo, 'r') as file:
        # Iteramos sobre cada línea del archivo
        for linea in file:
            # Dividimos la línea en tres partes: inicio, fin y costo
            inicio, fin, costo = linea.strip().split(',')
            # Convertimos el costo a un entero
            costo = int(costo)
            # Añadimos una arista al grafo desde la estación de inicio a la estación de fin con el costo asociado
            grafo.add_edge(inicio.strip(), fin.strip(), weight=costo)
    # Retornamos el grafo creado
    return grafo

# Función para encontrar las rutas más cortas utilizando Dijkstra
def encontrar_rutas(grafo, inicio):
    # Utilizamos el algoritmo de Dijkstra para encontrar las rutas más cortas desde la estación de inicio
    rutas = nx.single_source_dijkstra_path(grafo, inicio)
    # Calculamos los costos de las rutas más cortas
    costos = nx.single_source_dijkstra_path_length(grafo, inicio)
    # Iteramos sobre cada destino y su ruta asociada
    for destino, ruta in rutas.items():
        # Verificamos que el destino no sea igual a la estación de inicio
        if destino != inicio:
            # Obtenemos el costo total de la ruta
            costo_total = costos[destino]
            # Imprimimos la ruta y su costo total
            print(f"Desde {inicio} hasta {destino}: {ruta}, Costo total: {costo_total}")

# Función para mostrar las posibles destinos desde una estación de salida
def mostrar_destinos(grafo, inicio):
    # Obtenemos los vecinos de la estación de inicio en el grafo, que representan los posibles destinos
    destinos = list(grafo.neighbors(inicio))
    # Imprimimos los posibles destinos
    print(f"Posibles destinos desde {inicio}: {destinos}")

# Función para mostrar el grafo de las rutas más cortas utilizando Matplotlib
def mostrar_grafo_ruta_corta(grafo, inicio):
    # Utilizamos el algoritmo de Dijkstra para encontrar las rutas más cortas desde la estación de inicio
    rutas_cortas = nx.single_source_dijkstra_path(grafo, inicio)
    # Creamos un subgrafo que contenga solo las rutas más cortas
    subgrafo = grafo.subgraph(rutas_cortas)
    # Dibujamos el subgrafo utilizando Matplotlib
    nx.draw(subgrafo, with_labels=True, font_weight='bold')
    # Mostramos el grafo
    plt.show()

# Función principal
def main():
    # Definimos la ruta del archivo de rutas
    ruta_archivo = "C:/Users/Usuario/Documents/GitHub/Radio/HDT9-algoritmos/rutas.txt"
    # Creamos el grafo utilizando la función crear_grafo
    grafo = crear_grafo(ruta_archivo)
    
    # Ciclo principal del menú
    while True:
        # Imprimimos el menú
        print("\nMenú:")
        print("1. Ruta")
        print("2. Mostrar Grafo")
        print("3. Salir")
        # Solicitamos al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ").strip()

        # Opción para encontrar una ruta
        if opcion == '1': 
            # Solicitamos al usuario que ingrese la estación de salida
            inicio = input("Ingrese la estación de salida: ").strip()
            # Verificamos si la estación de salida está en el grafo
            if inicio not in grafo:
                print("Estación no encontrada. Por favor, ingrese una estación válida.")
                continue
            # Llamamos a la función encontrar_rutas para mostrar las rutas más cortas
            encontrar_rutas(grafo, inicio)
            continue

        # Opción para mostrar el grafo de las rutas más cortas
        elif opcion == '2':
            # Solicitamos al usuario que ingrese la estación de salida
            inicio = input("Ingrese la estación de salida: ").strip()
            # Verificamos si la estación de salida está en el grafo
            if inicio not in grafo:
                print("Estación no encontrada. Por favor, ingrese una estación válida.")
                continue
            # Llamamos a la función mostrar_grafo_ruta_corta para mostrar el grafo
            mostrar_grafo_ruta_corta(grafo, inicio)
            continue

        # Opción para salir del programa
        elif opcion == '3':
            break

        # Opción inválida
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Entrada al programa
if __name__ == "__main__":
    main()
