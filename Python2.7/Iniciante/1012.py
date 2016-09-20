#!usr/bin/env python
#-*- coding: utf-8 -*-

values = raw_input()
values = values.split(' ')
A = float(values[0])
B = float(values[1])
C = float(values[2])

print "TRIANGULO: {:0.3f}".format((A * C) / 2)
print "CIRCULO: {:0.3f}".format(3.14159 * (C**2))
print "TRAPEZIO: {:0.3f}".format(((A + B) * C) / 2)
print "QUADRADO: {:0.3f}".format(B**2)
print "RETANGULO: {:0.3f}".format(A * B)