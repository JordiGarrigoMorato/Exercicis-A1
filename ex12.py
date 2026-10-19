text = "Hello World"
text2 = "Hola mon!!!"

coincidencies = sum(1 for c1, c2 in zip(text, text2) if c1 == c2)

print(f"El text 1 és: '{text}'")
print(f"El text 2 és: '{text2}'")
print(f"Nombre de caràcters que coincideixen en la mateixa posició: {coincidencies}")