from random import randint
from random import uniform
import math
import matplotlib.pyplot as plt

arq = open("saida.txt",'w')

analise = 100
tamanho_pop = 200
tam_anticorpos = 3
melhores = []
prop_clone = 0.6
quantidade_Clones = int(tamanho_pop * 0.2)
geracoes = 100
taxaMutacao = 0.01

def popInicial():
	individuo = []
	for i in range(0,tamanho_pop):
		individuo.append([])
		for j in range(0, tam_anticorpos):
			a = uniform(-5.0,5.0)
			individuo[i].append(a)
	return individuo

def fitness(individuo):
	x = 0
	for j in range(0,tam_anticorpos):
		x += ((individuo[j])**2)
	return x


def selecaoClonal(pop, fitness, quantidade_Clones):
	clones = []
	fitness_aux = sorted(fitness)
	for i in range(0,quantidade_Clones):
		indice = fitness.index(fitness_aux[i])
		clones.append(pop[indice])
	return clones
		

def mutacaoClones(taxaMutacao, pop):
	fit_clone = list(map(fitness, pop))
	for j in range(0, len(fit_clone)):
		fit_clone[j] = abs(fit_clone[j])
	for i in range(0, len(pop)):
		aux = uniform(0, 1)
		if aux<=taxaMutacao:
			for k in range(0, len(pop[i])):
				pop[i][k] = uniform(-10 + min(pop[i]), 10-max(pop[i]))
	return pop

def atualizaPop(clones_mutados, pop, fit_pop):
	fitness_aux = sorted(fit_pop, reverse = True)
	for i in range(0,quantidade_Clones):
		indice = fit_pop.index(fitness_aux[i])
		pop[indice] = clones_mutados[i]
	return pop

def plota(melhores):
    x = []
    y = []

    for k in range(0,geracoes):
        x.append(k)
        y.append(melhores[k])
    fig,ax = plt.subplots()
    ax.plot(x,y)
    plt.show()

vetor_analise_min = []
vetor_analise_max = []

for j in range(0,analise):

	pop = popInicial()
	i=0
	melhores = []
	for i in range(0, geracoes):
		fit = list(map(fitness, pop))
		melhores.append(min(fit))
		clones = selecaoClonal(pop, fit, quantidade_Clones)
		clones_mutados = mutacaoClones(taxaMutacao, clones)
		pop = atualizaPop(clones_mutados, pop, fit)

	vetor_analise_min.append(min(melhores))
	vetor_analise_max.append(max(melhores))

arq.write("Menores valores: " + str(vetor_analise_min) + "\n")
arq.write("Maiores valores: " + str(vetor_analise_max) + "\n")
media_valores_max = sum(vetor_analise_max) / len(vetor_analise_max)
media_valores_min = sum(vetor_analise_min) / len(vetor_analise_min)
arq.write("Media dos maiores valores: " + str(media_valores_max) + "\n")
arq.write("Media dos menores valores: " + str(media_valores_min) + "\n")
arq.write("Maior valor: " + str(max(vetor_analise_max)) + "\n")
arq.write("Menor valor: " + str(min(vetor_analise_min)) + '\n')