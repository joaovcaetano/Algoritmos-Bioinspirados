from random import randint
from random import uniform
import math
import matplotlib.pyplot as plt


tamanho_populacao = 100
numero_individuos = 6
cr = 0.9
f = 1.0 #0.6
geracoes = 200
melhores = []
individuo = []

def popInicial():
	individuo = []
	for i in range(0,tamanho_populacao):
		individuo.append([])
		for j in range(0,numero_individuos):
			a = uniform(-50.0,50.0)
			individuo[i].append(a)
	return individuo
def fitness(individuo):
	x = 0
	for j in range(0,numero_individuos):
		x += (1.0/(individuo[j])**2)
	x = math.sqrt(x)
	z = x
	return z
def mutacao(individuo):
	x1 = 0
	x2 = 1
	x3 = 2
	while((x1 != x3) and (x1 != x2) and (x2 != x3)):
		x1 = uniform(0.0, float(tamanho_populacao))
		x2 = uniform(0.0, float(tamanho_populacao))
		x3 = uniform(0.0, float(tamanho_populacao))
		x1 = int(x1)
		x2 = int(x2)
		x3 = int(x3)
	ind1 = individuo[x1]
	ind2 = individuo[x2]
	ind3 = individuo[x3]
	for i in range(0,numero_individuos):
		ind1[i] = ind1[i] + f*(ind2[i] - ind3[i])
	return ind1 
def cruzamento(individuo, pop_inter):
	filhos = []
	for i in range(0,tamanho_populacao):
		filho = []
		for j in range(0, numero_individuos):
			random = uniform(0.0, 1.0)
			if(random < cr):
				filho.append(individuo[i][j])
			else:
				filho.append(pop_inter[i][j])
		filhos.append(filho)
	return filhos
def prox_geracao(individuo, filhos):
	novo_ind = []
	for i in range(0, len(individuo)):
		fit_pai = fitness(individuo[i])
		fit_filho = fitness(filhos[i])
		if (fit_pai < fit_filho):
			novo_ind.append(individuo[i])
		else:
			novo_ind.append(filhos[i])
	return novo_ind

def fit_geral(individuo):
	z = []
	for i in range(0,len(individuo)):
		x = 0
		for j in range(0,numero_individuos):
			x += (1.0/(individuo[i][j])**2)
		x = math.sqrt(x)
		z.append(x)
	return z
individuo = popInicial()
k = 0
while(k<geracoes):
	pop_int = []
	for i in range(0,tamanho_populacao):
		ind_int = mutacao(individuo)
		pop_int.append(ind_int)
	filhos = cruzamento(individuo, pop_int)
	novo_ind = prox_geracao(individuo, filhos)
	fit_melhor = fit_geral(novo_ind)
	print min(fit_melhor)
	k = k + 1
	individuo = novo_ind