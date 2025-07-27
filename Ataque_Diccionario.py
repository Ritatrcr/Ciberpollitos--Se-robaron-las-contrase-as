import hashlib
from tqdm import tqdm

# Lista de hashes objetivo (SHA-256)
hashes_objetivo = [
    "58a28ba457af0ff65b1ad6107efcc7d461eec2468d0515f89b84315aafcf5e6c",
    "2416a04204a49e90b413094b25883e029799e987843d6fd52d372e68d9aac5c0",
    "7dbe7c2245941a4fcf6a2e19ef6f3eff09bc047c2a4b2d7b055bde13dde5b48d",
    "10f6739d7539f4e955214c8757c18a1013aebfaf6e219aaa1e82b1508f0dd20a",
    "cf77f24652ade6eddf0c0a1f679faf630894a2d0c4fff45f91d1b7dcdc24a18f",
    "3365477c9456ea31f0edb0e35bb7f3427d3370786e882fe8345822df004e2c9c",
    "5e2b1605f42eef43322cca23761dd38aad4ce05c1a6ab83ccfd1301e53085d15",
    "6aaa2750836e5cf529f8a79c06235484790e2ce186ee8b5004a4652badbc5ff2",
    "e66e60760f76580de9f4372aeba03bfe133a186ed26f50574551bc02c21b1ff2",
    "90f553f5f64c65f9bcb8466ced049e199c919cf4d438c294b74501b5c454c163",
    "cc26507d9409ba52a19930045e604bf54d1d2e63b01b1e56dabedfe2f8a67123"
]

# Lista de años para combinar con las contraseñas
years = list(range(1995, 2026))

# Abrimos el archivo rockyou.txt y leemos las primeras 3000 contraseñas
rockyou_path = "rockyou.txt"  # Cambia esto si el archivo está en otro lugar
with open(rockyou_path, encoding='latin-1', errors='ignore') as f:
    lineas = [line.strip() for _, line in zip(range(3000), f)]

# Creamos una lista para guardar coincidencias
coincidencias = []

# Iteramos con barra de progreso
print("Buscando coincidencias...")
for idx, base in enumerate(tqdm(lineas)):

    # Por cada año, generamos una variante como 'contraseña1999*'
    for years in years:
        variante = f"{base}{years}*"
        
        # Calculamos el hash de la variante en SHA-256
        hash_variante = hashlib.sha256(variante.encode()).hexdigest()

        # Comparamos con cada hash objetivo
        if hash_variante in hashes_objetivo:
            coincidencias.append({
                'contraseña_base': base,
                'variante': variante,
                'hash': hash_variante,
                'posicion_rockyou': idx + 1
            })

# Mostramos los resultados
print("\n--- RESULTADOS ---")
for c in coincidencias:
    print(f"Encontrada: {c['variante']} (base: '{c['contraseña_base']}', pos: {c['posicion_rockyou']})")
    print(f"Hash: {c['hash']}\n")

# Guardamos los resultados en un archivo
with open("resultados.txt", "w") as out:
    for c in coincidencias:
        out.write(f"{c['variante']} | {c['hash']} | Base: {c['contraseña_base']} | Pos: {c['posicion_rockyou']}\n")

print("Proceso completado. Resultados guardados en 'resultados.txt'.")

