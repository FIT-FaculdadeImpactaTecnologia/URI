# -*- coding: utf-8 -*-

'''
Imagine que você tenha uma máquina do tempo que pode ser usada no máximo três vezes, e a cada uso da máquina você pode escolher 
voltar para o passado ou ir para o futuro. A máquina possui três créditos fixos; cada crédito representa uma certa quantidade de anos, 
e pode ser usado para ir essa quantidade de anos para o passado ou para o futuro. Você pode fazer uma, duas ou três viagens, 
e cada um desses três créditos pode ser usado uma vez apenas. Por exemplo, se os créditos forem 5, 12 e 9, 
você poderia decidir fazer duas viagens: ir 5 anos para o futuro e, depois, voltar 9 anos para o passado.
Dessa forma, você terminaria quatro anos no passado, em 2012. Também poderia fazer três viagens, todas indo para o futuro, 
usando os créditos em qualquer ordem, terminando em 2042.

Neste problema, dados os valores dos três créditos da máquina, seu programa deve dizer se é ou não possível viajar no tempo 
e voltar para o presente, fazendo pelo menos uma viagem e, no máximo, três viagens;
sempre usando cada um dos três créditos no máximo uma vez.

'''
i = raw_input()
a = i 
i = i.split()
n = a.split()
res = False
res2 = False
for j in range(len(i)): 
    n[j] = False
    # if( x.find(i[j]) ):
    if( n.count(i[j]) >= 1 ):
      res = True  
l = [0,0,0]      
l[0] = int(i[0])
l[1] = int(i[1])
l[2] = int(i[2])
 

l.sort()

# aux = int(i[0]) + int(i[1])     
aux = int(l[0]) + int(l[1])     

if( aux ==  int(l[2])):
    res2 = True
 
if(res == True or res2 == True):
    print 'S'
else:
    print 'N'

# print aux

# print i[j]
# print i

