# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import numpy


def prime_numbers(up_to):
    # 1 Gör en lista över alla tal från två till något valbart största tal n.
    prim_numbers = numpy.arange(2, up_to, 1)
    # 2 Stryk ut från listan alla jämna tal som är större än två (4, 6, 8 osv.)
    # 3 Listans nästa tal som inte är utstruket är ett primtal.
    # 4 Stryk ut alla tal, som är både större än det primtalet du hittade i föregående steget och multiplar av det.
    # 5 Upprepa stegen 3 och 4 tills du har nått ett nummer som är större än kvadratroten av n.

    start_index = 0
    lates_prime = prim_numbers[start_index]
    while lates_prime < numpy.sqrt(up_to):
        prim_numbers = prim_numbers[(prim_numbers % lates_prime != 0) | (prim_numbers <= lates_prime)]
        lates_prime = prim_numbers[start_index]
        start_index += 1
    # 6 Alla kvarstående tal i listan är primtal.
    return prim_numbers

def rotat(number):
    print(number)

def circular(n):
    print(str(n))
    print(len(str(n)))


if __name__ == '__main__':
    #prim = prime_numbers(2000000)
    circular(197)
    #for i in prim:
    #    print(i)
