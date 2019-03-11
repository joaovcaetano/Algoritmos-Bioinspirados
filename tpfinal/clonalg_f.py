#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import random
import numpy as np

# Leitura dos arquivos csv
capacidade = pd.read_csv('capacidades.csv', sep = '\t', header = None) # Capacidade dos locais (de votacao)
demandas = pd.read_csv('demandas.csv', sep = '\t', header = None)  # Demandas de cada setor(regiao)
distancias = pd.read_csv('distancias.csv', sep = ';', header = None) # Distancias regiao x local
maxDist = 1000000  # Distancia máxima admitida

#capacidade é uma matriz!!
#distancias i = locais j = setores
solucao = np.zeros((len(capacidade),), dtype=int)
capacidade_atual = solucao
solucao_zonas_atendidas = []

atendidas = []


#Gerando 1 indivíduo
for i in range(0, len(demandas[0])):
	pos_local = random.randint(0, 165)
	aux = demandas[0][i] + capacidade_atual[pos_local]
	print i
	while(capacidade[0][pos_local] < aux):
		pos_local = random.randint(0, 165)
		aux = demandas[0][i] + capacidade_atual[pos_local]
	capacidade_atual[pos_local] = demandas[0][i] + capacidade_atual[pos_local]
	solucao[pos_local] = solucao[pos_local] + distancias[pos_local][i]

#Só usar um list(map(fitness, populacao))

def fitness(individuo):
	fit = sum(individuo)
	return fit

