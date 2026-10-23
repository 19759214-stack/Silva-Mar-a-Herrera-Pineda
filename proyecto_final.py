# 1. ESTADO INICIAL
salud = 100
inventario = ["mapa"]
print(f"¡Bienvenido a la aventura! Tom empieza con {salud} de vida y su mochila tiene: {inventario}")

# 2. DECISIÓN DEL JUGADOR
camino = input("¿Quieres ir a la 'cueva' o al 'bosque'? ")

if camino == "cueva":
    print("¡Tom encontró una espada en la cueva! 🗡️")
    inventario.append("espada")
else:
    print("¡Unas espinas en el bosque hirieron a Tom! 🌿")
    salud = salud - 20

# 3. ENTRENAMIENTO Y RESULTADO FINAL
entrenamiento = 1
while entrenamiento <= 3:
    print(f"Tom realiza la ronda {entrenamiento} de entrenamiento... 🏋️")
    salud = salud + 10
    entrenamiento = entrenamiento + 1

print(f"¡Aventura completada! Tom terminó con {salud} de vida y su inventario final es: {inventario}")