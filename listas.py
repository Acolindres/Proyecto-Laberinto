lista_de_compras = ("manzanas", "bananos", "guayaba", "coca cola", "galletas")
lista_de_compras.sort()

print("Lista de compras:")
for i in lista_de_compras:
    print(i)

lista_de_compras.apppend("pastel")
lista_de_compras.sort()

print("\nlista de compras actualizada:")
for i in lista_de_compras:
    print(i)