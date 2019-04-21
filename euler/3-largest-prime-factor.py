'''
Problem statement:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Reference: https://projecteuler.net/problem=3

Notes:
Time complexity: O(n)
Space complexity: O(1)

How to run? :
python3 3-largest-prime-factor.py 600851475143
'''
import time
import sys
import math

def isPrime(x):
    for i in range(int(math.sqrt(x)),2,-1):
        if x%i == 0:
            return False
    return True

def getMaxPrimeFactor(num):
    for i in range(int(math.sqrt(num)),1,-1):
        if num%i == 0 and isPrime(i):
            return i

start_time = time.time()
max_prime_factor = getMaxPrimeFactor(int(sys.argv[1]))
print(max_prime_factor)
print("Execution time in seconds:",time.time() - start_time)