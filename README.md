# 🦕 Catálogo de Figuras Dino 🦖

## Cómo ejecutar el programa

Necesitas tener **Python 3** instalado en el ordenador.

1. Descarga o clona este repositorio.
2. Abre una terminal dentro de la carpeta del proyecto.
3. Ejecuta:

```bash
python main.py
```

En Windows también puedes utilizar:

```bash
py main.py
```

El programa se iniciará mostrando el menú principal y podrás seleccionar las diferentes opciones introduciendo su número.

🦖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🦕

## Objetivo

Este proyecto consiste en desarrollar un programa de consola en Python para gestionar un catálogo de figuras coleccionables con temática de dinosaurios.

## Contexto del catálogo

El catálogo está pensado para almacenar figuras de temática dinosaurios y otros artículos relacionados.

Cada figura contiene:

* **ID**
* **Nombre**
* **Categoría**
* **Precio**
* **Estado**
* **Descripción**

Los estados disponibles son `disponible`, `reservada` y `vendida`.

🦕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🦖

## Funcionalidades implementadas

El programa permite:

* Añadir nuevas figuras.
* Mostrar todas las figuras.
* Buscar una figura por su ID.
* Eliminar figuras.
* Comprobar si una figura existe.
* Filtrar figuras por estado.
* Filtrar figuras por precio mínimo.
* Obtener un resumen del catálogo por categorías.
* Buscar figuras por categoría.
* Calcular el precio medio.
* Validar los datos introducidos.

## Ejemplo de interacción

```text
🦖 🦕 🦖 🦕 🦖 🦕 🦖 🦕 🦖 🦕 🦖
1. Agregar nueva figura.
2. Mostrar todas las figuras.
3. Mostrar figuras disponibles.
4. Mostrar precio promedio.
5. Buscar una figura por su ID.
6. Eliminar una figura.
7. Salir.
🦖 🦕 🦖 🦕 🦖 🦕 🦖 🦕 🦖 🦕 🦖

Elige una opcion: 1
Introduce el ID de la figura: 1
Introduce el nombre de la figura: Rex
Introduce la categoría de la figura: Dinosaurio
Introduce el precio de la figura: 27.89
Introduce el estado de la figura: disponible
Introduce la descripción de la figura: Figura certificada

Figura agregada correctamente.
```

## Tecnologías utilizadas

* Python 3
* Consola/terminal
* Funciones
* Listas y diccionarios
* Bucles y condicionales
* Excepciones (`try` / `except`)
* Validación de datos
* Módulos e importación de funciones

🦖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🦕

## Estructura del proyecto

```text
catalogo-figuras-dino/
├── catalog.py
├── validations.py
├── main.py
└── README.md
```

* **`catalog.py`**: funciones para gestionar el catálogo.
* **`validations.py`**: funciones para validar los datos.
* **`main.py`**: menú principal e interacción con el usuario.
* **`README.md`**: documentación del proyecto.

🦕 **¡Gracias por visitar el Catálogo de Figuras Dino!** 🦖
