# -*- coding: utf-8 -*-
import random

nmin = 0
nmax = 80
nnumeros = 5
nsorteios = 5

# Gera nsorteios.
for i in range(0,nsorteios):
 l = []
 # Continua sorteando enquanto a lista não tiver nnumeros números.
 while len(l) < nnumeros:
  # sortear 1 números entre nmin e nmax.
  n = random.randint(nmin, nmax)
  if n not in l:
   l.append(n)
 # Organizar em ordem crescente.
 l.sort()
  # Printar número a número com espaço.
 for i in l:
  print(i, end=' ')
 print()