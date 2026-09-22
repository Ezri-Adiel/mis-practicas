lista = [8.5, 7.0, 9.5, 6.0, 7.8, 8.8, 10, 6.5, 9.0, 7.5, 8.2, 6.8, 9.2, 7.3, 8.0]
n = len(lista)
swapped = True
while swapped:
    swapped = False 
    for i in range (n-1):
        if lista[i] > lista [i+1]:
            lista [i], lista[i+1] = lista[i+1], lista[i]
            swapped = True
            print("Orden ascendente: ", lista)
