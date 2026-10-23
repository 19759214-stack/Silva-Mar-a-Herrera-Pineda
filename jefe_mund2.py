# 1. Pídele al usuario la energía actual de Tom usando int(input(...))
energia_actual = int(input("¿Cuánta energía tiene Tom (0-100)? "))

# 2. Si energia_actual >= 80:
if energia_actual >= 80:
    print("Tom está lleno de energía, ¡a correr y jugar afuera! ⚽")

# 3. Si no, pero energia_actual >= 40 (elif):
elif energia_actual >= 40:
    print("Tom tiene energía normal, ¡a ver televisión en el sofá! 📺")

# 4. Para cualquier otro caso (else):
else:
    print("Tom está agotado, ¡necesita dormir de inmediato! 💤")