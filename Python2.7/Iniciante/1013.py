#!usr/bin/env python
#-*- coding: utf-8 -*-

values = raw_input()
values = values.split(' ')
greater = 0

for item in values:
    if int(item) > int(greater):
        greater = int(item)

print "{} eh o maior".format(greater)