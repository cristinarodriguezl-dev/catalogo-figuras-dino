def validate_not_empty(value, field_name):
    if value.strip() == "":
        raise ValueError(f"El {field_name} no puede estar vacío")

def validate_name(name):
    validate_not_empty(name, "nombre")

def validate_price(price):
    if not isinstance(price, (float, int)):
        raise ValueError("El precio debe ser un número")
    if price <= 0:
        raise ValueError("El precio debe ser mayor que cero")

def validate_id(id):
    validate_not_empty(id, "ID")

def validate_status(status):
    if status != "disponible" and status != "reservada" and status != "vendida":
        raise ValueError("El estado debe ser 'disponible', 'reservada' o 'vendida'.")

def validate_category(category):
    validate_not_empty(category, "categoría")

def validate_description(description):
    if "certificada" not in description and "usada" not in description:
        raise ValueError("La descripción debe contener la palabra 'certificada' o 'usada'.")