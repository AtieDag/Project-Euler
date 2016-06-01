
import timeit
timer1 = timeit.timeit('list(range(0, 200000 - 1))', number=10)
print(timer1)
