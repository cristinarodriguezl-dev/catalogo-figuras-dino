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
    validate_id(id)
    for piece in catalog:
        if piece["id"] == id:
            return piece
    return None