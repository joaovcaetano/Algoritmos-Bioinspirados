from random import randint
from random import uniform
from igraph import *
import math
import matplotlib.pyplot as plt

def formigas(vertices, tamanho, quantidade):
	formigas = []
	for i in range(0, quantidade):
		random = randint(0, tamanho-1)
		formigas.append(random)
	return formigas

def vertices_faltantes(posicao, vertices):
	vertices_faltantes = []
	for i in range(posicao, len(vertices)):
		vertices_faltantes.append(vertices[i])
	return vertices_faltantes
grafo = Graph.Read_GraphML('dj38.gml')
vertices = grafo.vs['id']
tamanho = len(vertices)
quantidade = 10
formigas_pos = formigas(vertices, tamanho, quantidade)
lista_vertices = vertices_faltantes(0, vertices)
#Fazer pra todos as formigas
#Contador de posicao p formiga, vertice_faltante eh geral
#Como fazer a probabilidade??
