# Pandigital products

all_products = {}


def pandigital(multiplicand, multiplier):
    product = multiplier * multiplicand
    a = "".join(sorted(str(multiplier) + str(multiplicand) + str(product)))
    if a == "123456789":
        all_products[product] = product
        # print(str(multiplier) + str(multiplicand) + str(product))
    return a


for i in range(1, 1000):
    for j in range(10, int(10000 / i)):
        m = pandigital(i, j)

sums = 0
for key, value in all_products.items():
    sums += value

print(all_products, sums)
