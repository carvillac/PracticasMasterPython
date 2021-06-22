import pdb
pdb.set_trace()


def maximo(list):
    return [list[i] for i in range(0, len(list)) if (list[i-1] < list[i])][-1]


listas = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
max = [maximo(i) for i in listas]
print(max)
