'''
Problem statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Reference: https://projecteuler.net/problem=1

Notes:
Time complexity: O(n)
Space complexity: O(1)

How to run:
python3 1-sum-of-multiples-of-3-and-5.py 1000

'''
import sys
import time

start_time = time.time()

n= int(sys.argv[1])

i=1
sum = 0

for i in range(1,n):
    if i%3 == 0 or i%5 == 0 :
        sum += i

print(sum)

print("Execution time in seconds:",(time.time() - start_time))