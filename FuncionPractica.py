##Funcion sin parametros
def mostrar_encabezado_escuela():
    print("INSITITUTO X")
    print("REGISTRO Y EVALUACION DE CALIFICACONES")

##Funcion sin parametros
def obtener_nota_minima():
    return 6.0

##Funcion con parametros
def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif nota_final <= 9.4:
        return "Aprobado"
    else:
        return "Excelente"

##Funcion con parametros 2
def calcular_promedio_ponderado(nota_examenes,nota_tareas):
    promedio = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(promedio, 1)

#Funcion con parametros 3
def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):

    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)

    nota_minima = obtener_nota_minima()

    estado = evaluar_rendimiento (nota_final)
    print("Nombre del alumno", nombre_alumno)
    print("notal final", nota_final)
    print("estado", estado)
    if nota_final < nota_minima:
        print("Necesita presentar examen extraordinario para aprobar")
    else:
        print("Alumno aprobado no necesita examen extraordinario")

    mostrar_encabezado_escuela()
    generar_boleta("Juan", 8.5, 9.0)