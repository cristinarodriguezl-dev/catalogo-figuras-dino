from validations import *

def add_piece(id, name, category, price, status, description):
    validate_id(id)
    validate_name(name)
    validate_category(category)
    validate_price(price)
    validate_status(status)
    validate_description(description)


    return {"id": id, "name": name, "category": category, "price": price, "status": status, "description": description}

def list_pieces(catalog):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")
    
    names = []
    for piece in catalog:
        names.append(piece["name"])
    return names

def find_piece_by_id(catalog, id):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")

    validate_id(id)
    
    for piece in catalog:
        if piece["id"] == id:
            return piece
    return None

def remove_piece(catalog, id):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")

    validate_id(id)
    piece = find_piece_by_id(catalog, id)
    try:
        if piece is None:
            raise ValueError("Figura no encontrada")
        catalog.remove(piece)
        return True
    except ValueError:
        return False