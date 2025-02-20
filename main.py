from database import (
    initialize_database,
    add_book,
    update_book,
    delete_book,
    get_all_books,
    search_books,
)

def main_menu():
    print("\n=== Biblioteca Personal ===")
    print("1. Agregar nuevo libro")
    print("2. Actualizar información de un libro")
    print("3. Eliminar libro existente")
    print("4. Ver listado de libros")
    print("5. Buscar libros")
    print("6. Salir")

def handle_add_book():
    print("\n== Agregar nuevo libro ==")
    title = input("Título: ")
    author = input("Autor: ")
    genre = input("Género: ")
    status = input("Estado de lectura (leído/no leído): ").lower()
    if status not in ['leído', 'no leído']:
        print("Estado inválido. Por favor, escribe 'leído' o 'no leído'.")
        return
    add_book(title, author, genre, status)
    print("Libro agregado exitosamente.")

def handle_update_book():
    print("\n== Actualizar información de un libro ==")
    book_id = int(input("ID del libro a actualizar: "))
    print("Deja el campo vacío si no deseas modificarlo.")
    title = input("Nuevo título (opcional): ")
    author = input("Nuevo autor (opcional): ")
    genre = input("Nuevo género (opcional): ")
    status = input("Nuevo estado de lectura (leído/no leído, opcional): ").lower()
    update_book(book_id, title or None, author or None, genre or None, status or None)
    print("Libro actualizado exitosamente.")

def handle_delete_book():
    print("\n== Eliminar libro existente ==")
    book_id = int(input("ID del libro a eliminar: "))
    delete_book(book_id)
    print("Libro eliminado exitosamente.")

def handle_view_books():
    print("\n== Listado de libros ==")
    books = get_all_books()
    for book in books:
        print(f"ID: {book[0]}, Título: {book[1]}, Autor: {book[2]}, Género: {book[3]}, Estado: {book[4]}")

def handle_search_books():
    print("\n== Buscar libros ==")
    print("Buscar por: 1. Título  2. Autor  3. Género")
    option = int(input("Opción: "))
    if option == 1:
        field = "title"
    elif option == 2:
        field = "author"
    elif option == 3:
        field = "genre"
    else:
        print("Opción inválida.")
        return
    value = input(f"Introduce el {field} a buscar: ")
    books = search_books(field, value)
    for book in books:
        print(f"ID: {book[0]}, Título: {book[1]}, Autor: {book[2]}, Género: {book[3]}, Estado: {book[4]}")

def main():
    initialize_database()
    while True:
        main_menu()
        choice = input("Selecciona una opción: ")
        if choice == '1':
            handle_add_book()
        elif choice == '2':
            handle_update_book()
        elif choice == '3':
            handle_delete_book()
        elif choice == '4':
            handle_view_books()
        elif choice == '5':
            handle_search_books()
        elif choice == '6':
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")

if __name__ == "__main__":
    main()
