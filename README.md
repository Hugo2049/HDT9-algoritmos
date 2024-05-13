# HDT9-algoritmos
## Descripción

Este programa está diseñado para encontrar rutas más cortas en un sistema de transporte representado como un grafo ponderado. Utiliza el algoritmo de Dijkstra para encontrar las rutas más cortas desde una estación de salida dada.

## Autor

Hugo Ernesto Barillas Villagrán - 23306

## Requisitos

- Python 3.11
- Bibliotecas: NetworkX, Matplotlib

## Uso

1. **Ejecución del programa:**
  
  Para ejecutar el programa, simplemente ejecuta el archivo `main.py` en tu entorno de Python preferido.
  
  `python main.py`
  
2. **Menú:**
  
  El programa proporciona un menú interactivo con las siguientes opciones:
  
  - **Ruta:** Encuentra las rutas más cortas desde una estación de salida dada.
  - **Mostrar Grafo:** Muestra el grafo de las rutas más cortas desde una estación de salida dada.
  - **Salir:** Sale del programa.

## Funciones

1. **`crear_grafo(ruta_archivo):`**
  
  Lee un archivo de texto que contiene las rutas entre estaciones y crea un grafo ponderado.
  
2. **`encontrar_rutas(grafo, inicio):`**
  
  Encuentra y muestra las rutas más cortas desde una estación de salida dada utilizando el algoritmo de Dijkstra.
  
3. **`mostrar_destinos(grafo, inicio):`**
  
  Muestra los posibles destinos desde una estación de salida dada.
  
4. **`mostrar_grafo_ruta_corta(grafo, inicio):`**
  
  Muestra el grafo de las rutas más cortas desde una estación de salida dada utilizando Matplotlib.
  

## Archivo de Rutas

El programa espera un archivo de texto con el siguiente formato para definir las rutas

`estación_inicio,estación_fin,costo`

Donde:

- `estación_inicio` es el nombre de la estación de inicio.
- `estación_fin` es el nombre de la estación de destino.
- `costo` es el costo asociado a la ruta entre las dos estaciones.

## Errores
Algo que me pasó fue que para reconocer el pueblo debe ir exactamente como en el .txt ya que escribí "Pueblo paleta" y no "Pueblo Paleta" entonces no lo reconocio, por lo demás creo que bien.