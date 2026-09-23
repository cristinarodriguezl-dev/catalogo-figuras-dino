from validations import *

def add_piece(id, name, category, price, status, description):
    validate_id(id)
    validate_name(name)
    validate_category(category)
    validate_price(price)
    validate_status(status)
    validate_description(description)


    return {"id": id, "name": name, "category": category, "price": price, "status": status, "description": description}

