#!/usr/bin/python3
import random

"""
A-Z: 65d~90d
a-z: 97d-122d
"""
# print(''.join(chr(random.randint(65, 90)) for _ in range(4)))
# print(''.join(chr(random.randint(97, 122)) for _ in range(4)))

def genRandomStr(length):
    seed = 10
    result_str = []
    while len(result_str) < length:
        lower,upper = (65, 90) if random.randint(0,seed) % 2 is not 0 else (97, 122)
        result_str.append(chr(random.randint(lower, upper)))
    
    return ''.join(str(_) for _ in result_str)

print(genRandomStr(20))