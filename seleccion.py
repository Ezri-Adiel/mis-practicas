lista = [85, 70, 95, 60, 78, 88, 100, 65, 90, 75, 82, 68, 92, 73, 80]

n = len(lista)
swapped = True

while swapped:
    swapped = False
    for i in range(n-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            swapped = True

print("Orden Ascendente:", lista)
