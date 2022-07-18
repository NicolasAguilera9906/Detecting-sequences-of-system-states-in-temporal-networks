# import pandas
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def hamming_distance_matrix(num_nodos=None, grafo1=None, grafo2=None):
    A1 = nx.adjacency_matrix(grafo1).toarray()
    A2 = nx.adjacency_matrix(grafo2).toarray()
    distance_matrix = [[0 for j in range(num_nodos)] for i in range(num_nodos)]
    for i in range(num_nodos):
        for j in range(num_nodos):
            distance_matrix[i][j] = (1 / (num_nodos * (num_nodos - 1))) * abs(A1[i][j] - A2[i][j])
    return distance_matrix


def similarity_matrix(dis_matrix=None):
    max_value = max([max(x) for x in dis_matrix])
    dis_matrix_norm = [[dis_matrix[i][j] / max_value for j in range(len(dis_matrix[i]))]
                       for i in range(len(dis_matrix))]
    similarity_matrix = [[1 - dis_matrix_norm[i][j] / max_value for j in range(len(dis_matrix_norm[i]))]
                         for i in range(len(dis_matrix_norm))]
    return similarity_matrix


def print_similarity_matrix(similarity_matrix=None):
    fig, ax = plt.subplots(figsize=(20, 20))
    cax = ax.matshow(distance_matrix, interpolation='nearest')
    ax.grid(True)
    plt.title("Similarity matrix of the primary school")
    plt.xticks(range(len(similarity_matrix)), rotation=90)
    plt.yticks(range(len(similarity_matrix)))
    fig.colorbar(cax, ticks=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, .75, .8, .85, .90, .95, 1])
    plt.show()


# Importando Data Set de la Escuela Primaria
data_frame = pd.read_excel('data/primary_school_dataset.xlsx', )

grafos = []
tiempo_anterior = 31220
tiempo_actual = 0
grafo_temporal = nx.Graph()
nodos = set()
for index, data in data_frame.iterrows():
    tiempo_actual = int(data["t"])
    # Se genera un grafo distinto por cada intervalo de tiempo
    if tiempo_actual - tiempo_anterior >= 1200:
        # En el momento que el tiempo cambia se añade el grafo al diccionario de grafos
        grafos.append(grafo_temporal)
        grafo_temporal = nx.Graph()
        tiempo_anterior = tiempo_actual
    # Se extrae el ID de cada persona
    estudiante = data["i"]
    profesor = data["j"]
    nodos.add(estudiante)
    nodos.add(profesor)
    # Se añade la conexión al grafo
    grafo_temporal.add_edge(estudiante, profesor)
    grafo_temporal.add_edge(profesor, estudiante)
# Se añade el último grafo al diccionario de grafos que no alcanzó a entrar en el ciclo for.
if tiempo_actual - tiempo_anterior >= 1200:
    grafos.append(grafo_temporal)

for grafo in grafos:
    for nodo in nodos:
        grafo.add_node(nodo)


# Matriz de similaridad entre dos tiempos cualquiera dentro de la red
grafo2 = grafos[1]
grafo1 = grafos[0]
distance_matrix = hamming_distance_matrix(num_nodos=len(nodos), grafo1=grafo1, grafo2=grafo2)
similarity_matrix = similarity_matrix(dis_matrix=distance_matrix)
print(similarity_matrix)
print_similarity_matrix(similarity_matrix=similarity_matrix)
