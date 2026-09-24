##Ejemplo sin parametros
def mostrar_datos():
    print("Instituto Tecnológico")
    print("Materia: Estructura de Datos")
    print("Lenguaje: Python")

mostrar_datos()

##ejemplos con parametros

##Primera: 
def sumar(a, b):
    resultado = a + b
    print("La suma es:", resultado)

sumar(5, 3)


##Segunda:

def multiplicar(a, b):
    resultado = a * b
    print("La multiplicacion es:", resultado)

multiplicar(4, 6)

##Tercera 

def promedio(cal1, cal2, cal3):
    resultado = (cal1 + cal2 + cal3) / 3
    print("El promedio es:", resultado)

promedio(8.5, 9.0, 10.0)