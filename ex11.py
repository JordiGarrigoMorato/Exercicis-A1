textdna = "atggatcattta"
lletra_buscada = "a"

comptador = 0

print(f"Buscant la lletra '{lletra_buscada}' al text: '{textdna}'\n")
for index, lletra in enumerate(textdna):
    if lletra == lletra_buscada:
        comptador += 1
        print(f"Trobada '{lletra_buscada}' a la posició: {index}")

print(f"\nNombre total de vegades que apareix '{lletra_buscada}': {comptador}")