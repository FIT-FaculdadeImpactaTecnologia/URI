# -*- coding: utf-8 -*-
#2242

vog = "aeiou"

rs = raw_input()
aux = rs
for i in range(len(rs)):
    #print rs[i]
    if(vog.count(rs[i]) == 0):
        aux = aux.replace(rs[i],'') 

auxb = aux

if(auxb == aux[::-1]):  
    print "S"
else:
    print "N"



print aux



