# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


def prime_factors(number, a):
    print('number ', number, ' a ', a)
    while number != a or number < a:
        if number % a == 0:
            prime_factors(number / a, 2)
        else:
            a += 1
        if number == a:
            prime_factors(number / a, a)


prime_factors(600851475143,2)
