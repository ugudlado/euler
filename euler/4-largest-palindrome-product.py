'''
Problem statement:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Notes:
Time complexity: 
Space complexity:O(1)

How to run? :
python3 4-largest-palindrome-product.py 3
'''
import time
import math
import sys

def isPalindromeNumber(num):
    st = str(num)
    i = 0
    l = len(st)
    if(l < 2): return False
    while(i < l/2):
        if(st[i] != st[l-1-i]):
            return False
        i+=1
    return True

def isProductOfTwoNumbers(n,x):
    max_num = int(str(9)*n)
    min_num = int(str(1)*n)
    fac1 = 0
    for i in range(max_num,min_num,-1):
        if x % i == 0:
            if fac1 == 0:
                fac1 = i
            if fac1 != i and fac1 * i == x:
                return True
    return False

def maxPalindromeProductOfDigits(n):
    max_num = int(str(9)*n) * int(str(9)*n)
    min_num = int(str(1)*n) * int(str(1)*n)
    for i in range(max_num,min_num,-1):
        if isPalindromeNumber(i) and isProductOfTwoNumbers(n,i):
            return i

start_time = time.time()

num_of_digits= int(sys.argv[1])
max_palindrome_product = maxPalindromeProductOfDigits(num_of_digits)

print(max_palindrome_product)

print("Execution time in seconds:",time.time() - start_time)