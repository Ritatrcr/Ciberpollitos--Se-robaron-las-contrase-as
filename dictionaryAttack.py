import hashlib

# Lista de hashes SHA-256 robados
hashes_robados = {
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
}

# Cargar lista de contraseñas comunes desde Lista Contraseñas.txt
with open("Lista Contraseñas.txt", "r", encoding="latin-1", errors="ignore") as f:
    listaContraseñas= f.read()

    # Lee y limpia correctamente las contraseñas
    contraseñas_comunes = [pw.strip().strip('"').strip("'") for pw in listaContraseñas.split(",")]
    print(f"🔐 {len(contraseñas_comunes)} contraseñas cargadas desde 'Lista Contraseñas.txt'.\n")
    

    # Total de combinaciones por probar
    total_combinaciones = len(contraseñas_comunes) * (2025 - 1995 + 1)
    contador = 0

print(f"🔍 Iniciando prueba de {total_combinaciones} combinaciones...\n")

# Generar combinaciones y verificar
for base in contraseñas_comunes:
    for año in range(1995, 2026):
        combinacion = f"{base}{año}*"
        hash_generado = hashlib.sha256(combinacion.encode()).hexdigest()
        contador += 1

        
        # Si el hash coincide
        if hash_generado in hashes_robados:
            try:
                posicion_rockyou = contraseñas_comunes.index(base) + 1
            except ValueError:
                posicion_rockyou = None

            # Clasificación según posición
            if posicion_rockyou is None:
                categoria = "No encontrada en rockyou.txt"
            elif posicion_rockyou <= 100:
                categoria = " Muy común (Top 100)"
            elif posicion_rockyou <= 1000:
                categoria = "Común (Top 1000)"
            elif posicion_rockyou <= 3000:
                categoria = "Menos común (Top 3000)"
            else:
                categoria = f"Rara (posición {posicion_rockyou})"

            # Imprimir resultado encontrado
            print("¡Contraseña encontrada!")
            print(f"→ Combinación completa: {combinacion}")
            print(f"→ Hash coincidente: {hash_generado}")
            print(f"→ Contraseña base: {base}")
            if posicion_rockyou:
                print(f"→ Posición en rockyou.txt: {posicion_rockyou}")
            else:
                print("→ Posición en rockyou.txt: NO ENCONTRADA")
            print(f"→ Nivel de popularidad: {categoria}\n")
        