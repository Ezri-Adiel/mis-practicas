inventario_tech = ["Laptop", "Tarjeta de video", "Procesador", "Memoria RAM"]
inventario_tech.append("disco ssd")
inventario_tech.insert(2, "fuente de poder")
inventario_tech.extend(["gabinete", "monitor 4k", "teclado mecanico", "mouse gamer"])
print("monitor 4k" in inventario_tech)
print(inventario_tech.index("monitor 4k"))
inventario_tech[4] = "memoria RAM DDR5"
equipo_despachado = inventario_tech.pop()
inventario_tech.remove("Tarjeta de video")
print(equipo_despachado)
print(inventario_tech)
print(len(inventario_tech))