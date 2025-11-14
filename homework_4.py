class Book:
    format = "бумажная"

    def __init__(self, title, author, pages, format=None):
        self.title = title
        self.author = author
        self.pages = pages
        self.format = format or Book.format
    def __str__(self):
        return f"\"{self.title}\" — {self.author}, {self.pages} стр."


    def __len__(self):
        return self.pages


    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return f"Вместе: {self.pages + other.pages} страниц"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages == other.pages

    def __getitem__(self, chapter_num):
        return f"Глава {chapter_num}: содержание книги '{self.title}'"

    @classmethod
    def from_string(cls, s: str):
        title, author, pages = s.split(", ")
        return cls(title, author, int(pages))

    @staticmethod
    def is_thick(pages: int):
        return pages > 500


if __name__ == "__main__":

    book1 = Book("1984", "Дж. Оруэлл", 328)

    book2 = Book.from_string("Гарри Поттер, Дж. Роулинг, 400")

    print(book1)
    print(len(book1))
    print(book1 + book2)
    print(book1 == book2)
    print(book1[5])

    # Статический метод
    print(Book.is_thick(600))
    print(Book.is_thick(300))

    # Формат по умолчанию
    book3 = Book("Python", "Гвидо", 200)
    print(book3.format)
