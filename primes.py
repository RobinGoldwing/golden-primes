#!/bin/env python3

import os, sys, math



def isPrime(n):
    if n == 1: return False
    max = int(math.sqrt(n))
    for i in range(2,max):
        if (n % i) == 0 : return False
    return True

def prime():
    n = 1 
    while True:
        if isPrime(n):
            yield n
        n += 1
        
        
        
for primo in prime():
    print(primo, flush=True)

# maximo = int(input("Introduce el número máximo hasta el que buscar primos :"))
# for j in range (1,maximo):
#     if isprime(j): print(j)