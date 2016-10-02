# -*- coding: utf-8 -*-
vog = "aeiou"
rs = raw_input()
aux = rs
for i in range(len(rs)):
    if(vog.count(rs[i]) == 0):
        aux = aux.replace(rs[i],'') 
if(aux == aux[::-1]):  
    print "S"
else:
    print "N"

