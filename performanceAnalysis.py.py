import hashlib
import random
import time
from tqdm import tqdm

# Paso 1: Generar 50 números aleatorios únicos entre 1 y 100 millones
print("Generando 50 números aleatorios únicos...")
numeros_aleatorios = random.sample(range(1, 100_000_001), 50)

# Convertimos los números a strings y generamos sus hashes
hashes_objetivo = set()
for numero in numeros_aleatorios:
    hash_n = hashlib.sha256(str(numero).encode()).hexdigest()
    hashes_objetivo.add(hash_n)

print("Hashes de los 50 números generados.")

# Paso 2: Iniciar comparación
print("Iniciando comparación con 100 millones de números...")
inicio = time.time()

coincidencias = []
for i in tqdm(range(1, 100_000_001), desc="Comparando"):

    # Convertir número actual a string y hashearlo
    hash_actual = hashlib.sha256(str(i).encode()).hexdigest()

    # Verificar si está entre los hashes objetivo
    if hash_actual in hashes_objetivo:
        coincidencias.append((i, hash_actual))

fin = time.time()
tiempo_total = fin - inicio

# Paso 3: Mostrar resultados
print("\n--- RESULTADOS ---")
print(f"Tiempo total: {tiempo_total:.2f} segundos")
print(f"Coincidencias encontradas: {len(coincidencias)}")
for numero, hash_val in coincidencias:
    print(f"Coincidencia: {numero} -> {hash_val}")

# Paso 4: Guardar evidencias
with open("coincidencias_hashes.txt", "w") as f:
    f.write(f"Tiempo total: {tiempo_total:.2f} segundos\n")
    f.write(f"Coincidencias encontradas: {len(coincidencias)}\n\n")
    for numero, hash_val in coincidencias:
        f.write(f"{numero} -> {hash_val}\n")

print("Proceso completado. Resultados guardados en 'coincidencias_hashes.txt'.")
