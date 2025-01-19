BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int):
        if not isinstance(id, int):
            raise TypeError('Идентификатор книги должен быть типа "int"')
        if id < 0:
            raise ValueError('Идентификатор книги должен быть неотрицательным')
        self.id = id
        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа "str"')
        self.name = name
        if not isinstance(pages, int):
            raise TypeError('Количество страниц в книге должно быть типа "int"')
        if pages < 0:
            raise ValueError('Количество страниц в книге должно быть неотрицательным')
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
