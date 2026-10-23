# 1. Crea una variable llamada energia = 10
energia = 10

# 2. Escribe un bucle while que se ejecute mientras energia > 0
while energia > 0:
    # 3. Dentro del bucle:
    # Imprime el mensaje con el valor actual de energia usando f-string
    print(f"A Tom le quedan {energia} puntos de energía y sigue entrenando... 🏃")
    # Resta 2 puntos a la energía en cada vuelta
    energia = energia - 2

# 4. Fuera del bucle (sin sangría):
print("Tom se quedó sin energía y se fue a descansar 💤")