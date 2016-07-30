# Let p(n) represent the number of different ways in which n coins can be separated into piles.
# For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
# Find the least value of n for which p(n) is divisible by one million.


# The values of the partition function, p(0) = 1 and p(1) = 1.
partition_dict = {0: 1}


def partition_function(sign, part):
    if part in partition_dict:
        return sign * partition_dict[part]
    else:
        return 0


def pentagonal_number(k, mod):
    if mod == 1:
        return int(k * (3 * k + 1) / 2)
    else:
        return int(k * (3 * k - 1) / 2)


def partition(p):
    k = 1
    n = 0
    index = 0
    sums = 0
    while n < p:
        for a in range(2):
            index += 1
            n = pentagonal_number(k, a % 2)
            if (p - n) < 0:
                break
            value = partition_function((-1) ** (k - 1), p - n)
            if value == 0:
                value = partition(p - n)
                partition_dict[p - n] = value
            sums += value
        k += 1
    return sums


if __name__ == '__main__':
    partition_n = 2

    while True:
        partition(partition_n+1)
        print(partition_n)
        if partition_dict[partition_n] % 1000000 == 0:
            print(partition_n)
            break
        partition_n += 1
