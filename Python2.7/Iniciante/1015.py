#!usr/bin/env python
#-*- coding: utf-8 -*-
import math

X = raw_input()
Y = raw_input()
X = X.split(' ')
Y = Y.split(' ')
distancia = math.sqrt(((float(X[1]) - float(X[0])) ** 2) + ((float(Y[1]) - float(Y[0])) ** 2))
print "{:0.4f}".format(distancia)