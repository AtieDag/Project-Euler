# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math
import numpy

up_to = 100
# 1 Gör en lista över alla tal från två till något valbart största tal n.
prim_numbers = numpy.arange(2, up_to, 1)
# 2 Stryk ut från listan alla jämna tal som är större än två (4, 6, 8 osv.)
# 3 Listans nästa tal som inte är utstruket är ett primtal.
# 4 Stryk ut alla tal, som är både större än det primtalet du hittade i föregående steget och multiplar av det.
# 5 Upprepa stegen 3 och 4 tills du har nått ett nummer som är större än kvadratroten av n.

start_value = 2
start_index = 2
while start_value <= math.sqrt(up_to)+1:
    # 5 Upprepa stegen 3 och 4 tills du har nått ett nummer som är större än kvadratroten av n

    index = numpy.arange(start_value, up_to, start_index)
    prim_numbers = numpy.delete(prim_numbers, index)
    start_value += 2
    start_index += 1

    print(prim_numbers)

# 6 Alla kvarstående tal i listan är primtal.
print(sum(prim_numbers))

