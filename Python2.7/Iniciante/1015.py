#!usr/bin/env python
#-*- coding: utf-8 -*-
import math

p1 = raw_input()
p2 = raw_input()
p1 = p1.split(' ')
p2 = p2.split(' ')
distancia = math.sqrt(((float(p2[0]) - float(p1[0])) ** 2) + ((float(p2[1]) - float(p1[1])) ** 2))
print "{:0.4f}".format(distancia)