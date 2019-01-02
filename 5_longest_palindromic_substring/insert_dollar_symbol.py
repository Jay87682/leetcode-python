#!/usr/bin/python3


s = 'test123'
special_symb = '$'

after_insert_s = ''.join(map(str, [special_symb+char for char in s])) + special_symb

#for x in s:
#	after_insert_s = after_insert_s + x

print(after_insert_s)
