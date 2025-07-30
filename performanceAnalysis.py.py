import hashlib
import random
import time

# Generar 50 números aleatorios únicos entre 1 y 100 millones
print("Generando 50 números aleatorios únicos...")
numeros_aleatorios = random.sample(range(1, 100_000_001), 50)

# Convertir los números a strings y generar sus hashes
hashes_objetivo = set()
for numero in numeros_aleatorios:
    hash_n = hashlib.sha256(str(numero).encode()).hexdigest()
    hashes_objetivo.add(hash_n)

print("Hashes de los 50 números generados.")

# Iniciar comparación
print("Iniciando comparación con 100 millones de números...")
inicio = time.time()

coincidencias = []
for i in range(1, 100_000_001):
    hash_actual = hashlib.sha256(str(i).encode()).hexdigest()
    if hash_actual in hashes_objetivo:
        coincidencias.append((i, hash_actual))

tiempo_total = time.time() - inicio

# Mostrar resultados
print("\n--- RESULTADOS ---")
print(f"Tiempo total: {tiempo_total:.2f} segundos")
print(f"Coincidencias encontradas: {len(coincidencias)}")
for numero, hash_val in coincidencias:
    print(f"Coincidencia: {numero} -> {hash_val}")