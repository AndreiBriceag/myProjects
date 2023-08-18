import math

def is_prime2(num):
    '''
    Better method of checking for primes.
    '''
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
        
    return True

print(is_prime2(157))

# def is_prime(num):
#     '''
#     bad method of checking for primes.
#     '''
#     for n in range(2, num):
#         if num % n == 0:
#             print(num, 'is not prime')
#             break
#     else:  # If never mod zero, then prime
#         print(num, 'is prime!')

# is_prime(99)
