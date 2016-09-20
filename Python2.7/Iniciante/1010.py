#!usr/bin/env python
#-*- coding: utf-8 -*-

peca1 = raw_input()
peca1 = peca1.split(' ')
peca2 = raw_input()
peca2 = peca2.split(' ')

total = (int(peca1[1]) * float(peca1[2])) + (int(peca2[1]) * float(peca2[2]))

print "VALOR A PAGAR: R$ {:0.2f}".format(total)