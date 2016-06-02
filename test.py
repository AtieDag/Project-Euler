import numpy
import timeit
timer1 = timeit.timeit('list(range(0, 200000 - 1))', number=10)
print(timer1)


up_to = 200

prim_numbers = numpy.arange(2, up_to, 1)

sum_prime = 0
for prime in numpy.ndenumerate(prim_numbers):
    print(prime)
