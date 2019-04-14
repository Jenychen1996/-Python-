#-*- encoding:utf-8 -*-

"""
方式一
"""
"""
def is_primes(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
                return True

def sum_primes(value):
    result = sum(each for each in range(2, value) if is_primes(each))
    print(result)

sum_primes(2000000)
"""
"""
方式二
"""

def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True
    else:
        return False

def get_prime(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve():
    total = 2
    for next_prime in get_prime(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

if __name__ == '__main__':
    solve()

