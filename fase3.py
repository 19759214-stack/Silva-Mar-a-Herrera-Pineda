# 1. Crea la variable entrenamiento = 1
entrenamiento = 1

# 2. Escribe un bucle while entrenamiento <= 3
while entrenamiento <= 3:
    # Imprime el mensaje de la ronda usando f-string
    print("Tom realiza la ronda {entrenamiento} de entrenamiento... 🏋️")
    # Aumenta la salud en 10 puntos
    salud = salud + 10
    # Suma 1 al contador para avanzar de ronda
    entrenamiento = entrenamiento + 1

# 3. Fuera del bucle (sin sangría), muestra el mensaje final con f-string
print("¡Aventura completada! Tom terminó con {salud} de vida y su inventario final es: {inventario}")