from catalog import add_piece, list_pieces, get_average_price, find_piece_by_id, remove_piece, filter_by_status
from validations import validate_id, validate_name, validate_category, validate_price, validate_status, validate_description


def ask_for_value(message, validation, converter=str):
    while True:
        try:
            value = input(message)
            value = converter(value)
            validation(value)
            return value
        except ValueError as error:
            print(f"Error: {error}")


catalog = []

while True:
    print("\n*******************************")
    print("1. Agregar nueva figura.")
    print("2. Mostrar todas las figuras.")
    print("3. Mostrar figuras disponibles.")
    print("4. Mostrar precio promedio.")
    print("5. Buscar una figura por su ID.")
    print("6. Eliminar una figura.")
    print("7. Salir.")
    print("*******************************")

    option = input("Elige una opcion: ")

    if option == "1":
        id = ask_for_value(
            "Introduce el ID de la figura: ",
            validate_id
        )

        name = ask_for_value(
            "Introduce el nombre de la figura: ",
            validate_name
        )

        category = ask_for_value(
            "Introduce la categoría de la figura: ",
            validate_category
        )

        price = ask_for_value(
            "Introduce el precio de la figura: ",
            validate_price,
            lambda value: float(value.replace(",", "."))
        )

        status = ask_for_value(
            "Introduce el estado de la figura: ",
            validate_status
        )

        description = ask_for_value(
            "Introduce la descripción de la figura: ",
            validate_description
        )

        piece = add_piece(
            id,
            name,
            category,
            price,
            status,
            description
        )

        catalog.append(piece)

        print("Figura agregada correctamente.")

    elif option == "2":
        try:
            print(list_pieces(catalog))
        except ValueError as error:
            print(f"Error: {error}")

    elif option == "3":
        try:
            print(filter_by_status(catalog, "disponible"))
        except ValueError as error:
            print(f"Error: {error}")

    elif option == "4":
        try:
            print(get_average_price(catalog))
        except ValueError as error:
            print(f"Error: {error}")

    elif option == "5":
        try:
            id = input("Introduce el ID de la figura: ")
            piece = find_piece_by_id(catalog, id)

            if piece:
                print(piece)
            else:
                print("Figura no encontrada")

        except ValueError as error:
            print(f"Error: {error}")

    elif option == "6":
        try:
            id = input("Introduce el ID de la figura: ")

            if remove_piece(catalog, id):
                print("Figura eliminada correctamente")
            else:
                print("Figura no encontrada")

        except ValueError as error:
            print(f"Error: {error}")

    elif option == "7":
        print("Hasta luego")
        break

    else:
        print("Opcion invalida")