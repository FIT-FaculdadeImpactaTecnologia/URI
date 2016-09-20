#!usr/bin/env python
#-*- coding: utf-8 -*-

nome = raw_input()
fixo = input()
vendas = input()

comissao = (vendas * 0.15)

print "TOTAL = R$ {:0.2f}".format((fixo + comissao)) 
