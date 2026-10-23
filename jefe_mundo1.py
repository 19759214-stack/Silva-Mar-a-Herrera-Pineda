# 1. Pide el nombre del bocadillo y guárdalo en 'alimento'
alimento = input("¿Qué bocadillo le darás a Tom? ")

# 2. Pide los puntos de energía y conviértelos a entero con int()
energia_ganada = int(input("¿Cuántos puntos de energía da ese bocadillo? "))

# 3. Calcula la energía total sumando los 20 puntos iniciales
energia_total = 20 + energia_ganada

# 4. Muestra el mensaje final usando un print() con f-string
print(f"Tom comió {alimento} y ahora tiene {energia_total} puntos de energía.")