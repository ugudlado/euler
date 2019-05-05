'''
Problem statement:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Notes:
Time complexity: 
Space complexity: 

How to run? :
python3 5-find-lcm-of-multiple-numbers.py
'''
import time
import sys

start_time = time.time()

def lcm(a, b):
    return int(a*b/gcd(a,b))

def gcd (a, b):
    while(1):
        if( a == 0 ): return b
        if (b == 0 ): return a

        if (a == 1 or b ==1 ): return 1
        
        if(a > b):
            a = a-b
        else:
            b = b-a

n = int(sys.argv[1])
l = 1
for i in range(2,n+1):
     l = lcm(l,i)

print(l)
print("Execution time in seconds:",time.time() - start_time)