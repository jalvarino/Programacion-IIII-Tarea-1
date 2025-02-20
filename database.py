import sqlite3

# Conexión inicial a la base de datos
def initialize_database():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    # Crear tabla de libros si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

# Agregar un libro
def add_book(title, author, genre, status):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author, genre, status) VALUES (?, ?, ?, ?)",
                   (title, author, genre, status))
    connection.commit()
    connection.close()

# Actualizar información de un libro
def update_book(book_id, title=None, author=None, genre=None, status=None):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    if title:
        cursor.execute("UPDATE books SET title = ? WHERE id = ?", (title, book_id))
    if author:
        cursor.execute("UPDATE books SET author = ? WHERE id = ?", (author, book_id))
    if genre:
        cursor.execute("UPDATE books SET genre = ? WHERE id = ?", (genre, book_id))
    if status:
        cursor.execute("UPDATE books SET status = ? WHERE id = ?", (status, book_id))
    connection.commit()
    connection.close()

# Eliminar un libro
def delete_book(book_id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()
    connection.close()

# Ver todos los libros
def get_all_books():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connection.close()
    return books

# Buscar libros por título, autor o género
def search_books(field, value):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    query = f"SELECT * FROM books WHERE {field} LIKE ?"
    cursor.execute(query, ('%' + value + '%',))
    books = cursor.fetchall()
    connection.close()
    return books
