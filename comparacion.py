import matplotlib.pyplot as plt

# Datos de prueba originales
datos = [42, 12, 88, 23, 7, 65, 34, 50]

# --- ALGORITMO DE INSERCIÓN ---
def insercion(arr):
    a = arr.copy()
    comp = 0
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        
        # Validación de la primera comparación del ciclo
        if j >= 0:
            comp += 1
            
        while j >= 0 and a[j] > clave:
            a[j + 1] = a[j]
            j -= 1
            # Si el ciclo continúa, cuenta la siguiente comparación
            if j >= 0 and a[j] > clave:
                comp += 1
                
        a[j + 1] = clave
    # CORREGIDO: El return va alineado con el 'for' (al final de toda la función)
    return a, comp


# --- ALGORITMO DE SELECCIÓN ---
def seleccion(arr):
    # CORREGIDO: Se cambió 'rr.copy()' por 'arr.copy()'
    a = arr.copy()
    comp = 0
    # CORREGIDO: Se define 'n' para que no marque error de variable inexistente
    n = len(a)  
    
    for i in range(n):
        min_idx = i  # CORREGIDO: Se unificó a 'min_idx' (antes tenías min_idnx)
        for j in range(i + 1, n):
            comp += 1
            if a[j] < a[min_idx]:
                min_idx = j
        # CORREGIDO: El intercambio de valores se hace fuera del bucle de 'j'
        a[i], a[min_idx] = a[min_idx], a[i]
        
    # CORREGIDO: El return va al final de la función, alineado con el primer 'for'
    return a, comp 


# --- EJECUTAMOS LOS 2 ALGORITMOS ---
lista_ordenada, comp_ins = insercion(datos)
_, comp_sel = seleccion(datos)


# --- GRAFICACIÓN CON MATPLOTLIB ---
# CORREGIDO: Se cambió 'subplot' por 'subplots' (con 's' al final)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

# GRÁFICO 1: LISTA DESORDENADA
ax1.bar(range(len(datos)), datos, color='red')
ax1.set_title('1. LISTA ORIGINAL')
ax1.set_ylabel('Valor')

# GRÁFICO 2: LISTA ORDENADA
# CORREGIDO: Se eliminó el paréntesis roto de 'range(len)(lista_ordenada)'
ax2.bar(range(len(lista_ordenada)), lista_ordenada, color='blue')
ax2.set_title('2. LISTA ORDENADA')

# GRÁFICO 3: COMPARACIONES REALIZADAS
ax3.bar(['Inserción', 'Selección'], [comp_ins, comp_sel], color=['#175b8b', '#b6733a'])
ax3.set_title('3. COMPARACIONES')
ax3.set_ylabel('Cantidad')

plt.tight_layout()
plt.show()
