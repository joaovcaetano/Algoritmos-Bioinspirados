from random import randint
from random import uniform
from igraph import *
import math
import matplotlib.pyplot as plt

def popInicial(vertices, quantidade):
	populacao = []
	for i in range(0,quantidade):
		individuo = []
		for j in range(0, tamanho_individuo):
			random = int(uniform(0.0, float(tamanho_individuo)))
			if vertices[random] not in individuo:
				individuo.append(vertices[random])
			else:
				random = int(uniform(0.0, float(tamanho_individuo)))
				while(vertices[random] in individuo):
					random = int(uniform(0.0, float(tamanho_individuo)))
				individuo.append(vertices[random])
		populacao.append(individuo)
	return populacao

def fitness(individuo, vertices):
	distancia_total = 0
	for i in range(0, len(individuo)):
		par = []
		pesos = []
		if i == (len(individuo) -1):
			v1 = vertices.index(individuo[i])
			par.append(v1)
			v2 = vertices.index(individuo[0])
			par.append(v2)
		else:
			v1 = vertices.index(individuo[i])
			par.append(v1)
			v2 = vertices.index(individuo[i+1])
			par.append(v2)
		arestas = grafo.get_eid(par[0], par[1])
		peso = grafo.es[arestas]['weight']
		distancia_total = peso + distancia_total
	return int(distancia_total)

def roleta(porcentagem_individual):
	roleta = uniform(0.0, 1.0)
	soma = 0
	j = 0
	while(soma <= roleta):
		soma = soma + porcentagem_individual[j]
		j = j + 1
	pos_pai = j - 1
	return pos_pai

def selecao(total_fit, tam_pop):
	porcentagem_individual = []
	aux = []
	for i in range(0, len(total_fit)):
	 	aux.append(float(1)/float(total_fit[i]))
	total = sum(aux)
	for i in range(0,tam_pop):
		porcent = float(aux[i]) / float(total)
		porcentagem_individual.append(porcent)
	pai1 = roleta(porcentagem_individual)
	pai2 = roleta(porcentagem_individual)
	if pai2 == pai1:
		pai2 = roleta(porcentagem_individual)
		while(pai2 == pai1):
			pai2 = roleta(porcentagem_individual)
	pais = []
	pais.append(pai1)
	pais.append(pai2)
	return pais

def pontos():
	p1 = int(uniform(0.0, float(tamanho_individuo-1)))
	p2 = int(uniform(0.0, float(tamanho_individuo-1)))
	if (p2 == p1):
		p2 = int(uniform(0.0, float(tamanho_individuo-1)))
		while(p2 == p1):
			p2 = int(uniform(0.0, float(tamanho_individuo-1)))
	pontos = []
	pontos.append(p1)
	pontos.append(p2)
	pontos = sorted(pontos)
	if pontos[0] == 0:
		pontos[0] = 1
	if pontos[1] == tamanho_individuo - 1:
		pontos[1] == tamanho_individuo - 2
	if((pontos[1] - pontos[0]) == 1):
		pontos[1] = pontos[1] + 1
	return pontos
def cruzamento(pais, populacao):
	filhos = []
	filho1 = []
	filho2 = []
	p = pontos()
	pai1 = populacao[pais[0]]
	pai2 = populacao[pais[1]]
	mp1 = []
	mp2 = []
	for i in range(p[0], p[1]):
		mp1.append(pai1[i])
		mp2.append(pai2[i])
	for i in range(0, p[0]):
		if pai1[i] not in mp1:
			filho1.append(pai1[i])
		if pai2[i] not in mp2:
			filho2.append(pai2[i])
	for i in range(p[0], p[1]):
		filho1.append(pai1[i])
		filho2.append(pai2[i])
	for i in range(p[1], tamanho_individuo):
		if (pai1[i] not in filho1):
			filho1.append(pai1[i])
		if (pai2[i] not in filho2):
			filho2.append(pai2[i])
	filhos.append(filho1)
	filhos.append(filho2)
	return filhos

def mutacao(populacao, taxa):
	for i in range(0,len(populacao)):
		random = uniform(0.0, 1.0)
		if random < taxa:
			for j in range(0, tamanho_individuo):
				rand = uniform(0.0, 1.0)
				if random < taxa:
					rand3 = int(uniform(0.0, float(tamanho_individuo)))
					aux = populacao[i][j]
					populacao[i][j] = populacao[i][rand3]
					populacao[i][rand3] = aux
	return populacao

grafo = Graph.Read_GraphML('dj38.gml')
vertices = grafo.vs['id']
tamanho_individuo = len(vertices)
tam_pop = 500
geracoes = 4000
taxa_mutacao = 0.05
melhores = []
k = 0
pop_atual = popInicial(vertices, tam_pop)
while(k < geracoes):
	fit_geral = []
	filhos = []
	fit_geral_filho = []
	for i in range(0, tam_pop):
		fit_ind = fitness(pop_atual[i], vertices)
		fit_geral.append(fit_ind)
	melhores.append(min(fit_geral))
	indice_melhor = fit_geral.index(min(fit_geral))
	aux = pop_atual[indice_melhor]
	for i in range(0, (int(tam_pop/2))):
		pais = selecao(fit_geral, tam_pop)
		filho = cruzamento(pais, pop_atual)
		filhos.append(filho[0])
		filhos.append(filho[1])
	filhos = mutacao(filhos, taxa_mutacao)
	pop_atual = filhos
	for i in range(0, tam_pop):
		fit_ind_filho = fitness(pop_atual[i], vertices)
		fit_geral_filho.append(fit_ind_filho)
	indice_pior = fit_geral_filho.index(max(fit_geral_filho))
	pop_atual[indice_pior] = aux
	k = k + 1
print melhores
