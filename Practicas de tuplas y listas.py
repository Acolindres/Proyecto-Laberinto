# Crea una lista llamada lista_de_compras con al menos cinco ítems que necesites comprar
lista_de_compras = ["manzanas", "bananos", "guayaba", "coca cola", "galletas"]
def imprimir():
  for item in lista_de_compras:
    print(item)
imprimir()

print(f"\nMe gusto el pastel que probe ayer lo añadire a la lista. \n")

lista_de_compras.append("pastel")

print("lista actualizada")

imprimir()

