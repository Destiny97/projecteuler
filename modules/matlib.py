import math

# primes
def isPrime(n):
    if (not isinstance(n, int) and not isinstance(n, float) and n%1 != 0) or n <= 1: return False
    elif n <= 3: return True
    elif n%2 == 0 or n%3 == 0: return False

    i = 5
    sn = math.ceil(math.sqrt(n))
    while i <= sn:
        if n%i == 0 or n%(i+2) == 0: return False
        i += 6
    return True

def nextPrime(n):
    n += 1
    while not isPrime(n):
        n += 1
    return n

def primeFactors(n):
    fact = [] # prime fators of n
    while not isPrime(n):
        x = 2 # tested number
        while n%x != 0: x = nextPrime(x)
        fact.append(x)
        n /= x
    fact.append(int(n))
    return fact

# palindromes
def isPalindrome(n):
    n = str(n)
    return n == n[::-1]
