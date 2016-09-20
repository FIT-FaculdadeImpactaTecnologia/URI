#!usr/bin/env python
#-*- coding: utf-8 -*-

funcionario = input() 
horas = input()
valor_hora = input()

print "NUMBER = " + str(funcionario)
print "SALARY = U$ {:0.2f}".format(valor_hora * horas)