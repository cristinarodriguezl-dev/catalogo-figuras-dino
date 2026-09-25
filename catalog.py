from validations import validate_category
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

def get_catalog_summary(catalog):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")
    
    summary = {}

    for piece in catalog:
        category = piece["category"]
        if category in summary:
            summary[category] += 1
        else:
            summary[category] = 1
    return summary

def get_pieces_by_category(catalog, category):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")

    names = []

    for piece in catalog:
        if piece["category"] == category:
            names.append(piece["name"])

    return names

def piece_exists(catalog, id):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")
    validate_id(id)

    piece = find_piece_by_id(catalog, id)

    if piece is not None:
        return True
    return False

def filter_by_status(catalog, status):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")
    
    validate_status(status)

    filtered_catalog = []
    for piece in catalog:
        if piece["status"] == status:
            filtered_catalog.append(piece)
    return filtered_catalog

def filter_by_min_price(catalog, price):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")
    validate_price(price)
    
    filtered_catalog = []
    for piece in catalog:
        if piece["price"] > price:
            filtered_catalog.append(piece)
    return filtered_catalog

def get_average_price(catalog):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")
    if len(catalog) == 0:
        return 0
    total_price = 0
    for piece in catalog:
        total_price += piece["price"]
    return total_price / len(catalog)