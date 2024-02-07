class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def name(self) -> str:
        return self.name

    def author(self) -> str:
        return self.author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def pages(self) -> int:
        return self.pages

    def pages(self, value: int) -> None:
        self.pages = value
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Кол-во страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def duration(self) -> float:
        return self.duration

    def duration(self, value: float) -> None:
        self.duration = value
        if not isinstance(value, float):
            raise TypeError
        if value <= 0:
            raise ValueError

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self.duration}ч."
