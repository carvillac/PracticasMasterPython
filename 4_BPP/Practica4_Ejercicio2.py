def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


numeros = [3, 4, 8, 5, 5, 22, 13]

primos = list(filter(es_primo, numeros))
print(primos)
