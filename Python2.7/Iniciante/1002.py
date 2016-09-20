#!usr/bin/env python
#-*- coding: utf-8 -*-

def area(r):
    return 3.14159 * (r**2)

r = input()

print 'A={:0.4f}'.format(area(r))