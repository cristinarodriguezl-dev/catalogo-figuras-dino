def validate_name(name):
    if name.strip() == "":
        raise ValueError("El nombre no puede estar vacío")

def validate_price(price):
    if not isinstance(price, (float, int)):
        raise ValueError("El precio debe ser un número")
    if price <= 0:
        raise ValueError("El precio debe ser mayor que cero")

def validate_id(id):
    if id.strip() == "":
        raise ValueError("El ID no puede estar vacío")

def validate_status(status):
    if status != "disponible" and status != "reservada" and status != "vendida":
        raise ValueError("El estado debe ser 'disponible', 'reservada' o 'vendida'.")

def validate_category(category):
    if category.strip() == "":
        raise ValueError("La categoría no puede estar vacía")

def validate_description(description):
    if "certificada" not in description and "usada" not in description:
        raise ValueError("La descripción debe contener la palabra 'certificada' o 'usada'.")