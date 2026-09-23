from catalog import add_piece, list_pieces

#Prueba

catalog = []
piece1 = add_piece("1", "Tyrannosaurus Rex", "figura", -5, "disponible", "Figura usada en buen estado")
catalog.append(piece1)

print(list_pieces(catalog))