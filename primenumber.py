import numpy as np

# 1 Gör en lista över alla tal från två till något valbart största tal n.
# 2 Stryk ut från listan alla jämna tal som är större än två (4, 6, 8 osv.)
# 3 Listans nästa tal som inte är utstruket är ett primtal.
# 4 Stryk ut alla tal, som är både större än det primtalet du hittade i föregående steget och multiplar av det.
# 5 Upprepa stegen 3 och 4 tills du har nått ett nummer som är större än kvadratroten av n.

prim_numbers = []

def update_prime_array(new_value):
    global prim_numbers
    prime_len = len(prim_numbers)
    end_value = prim_numbers[prime_len - 1]
    if end_value < new_value:
        prim_numbers = np.insert(prim_numbers, prime_len, np.arange(prime_len, new_value, 1), 0)


def update_prime_list(up_to=500):
    global prim_numbers
    if len(prim_numbers) == 0:
        start_index = 0
    else:
        start_index = prim_numbers[len(prim_numbers)-1]

    update_prime_array(up_to)
    lates_prime = prim_numbers[start_index]
    while lates_prime < np.sqrt(up_to):
        prim_numbers = prim_numbers[(prim_numbers % lates_prime != 0) | (prim_numbers <= lates_prime)]
        lates_prime = prim_numbers[start_index]
        print(lates_prime)
        start_index += 1


# 6 Alla kvarstående tal i listan är primtal.
if __name__ == '__main__':
    update_prime_list(20)
    print(prim_numbers)
    update_prime_list(100)
    print(prim_numbers)
    #update_prime_list(400)
    #print(prim_numbers)
