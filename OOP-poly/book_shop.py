class Book:
    def __init__(self, author: str, title: str, price: float):
        self.author = author
        self.title = title
        self.price = price

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        names = value.split(" ")
        if len(names) > 1:
            last_n = names[1]

            if last_n[0].isdigit():
                print("Author not valid!")
                exit(0)
            else:
                self.__author = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) < 3:
            print("Title not valid!")
            exit(0)
        else:
            self.__title = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Price not valid!")
            exit(0)
        else:
            self.__price = value

    def __str__(self):
        return f"Type: {self.__class__.__name__}\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}\n"


class GoldenEditionBook(Book):
    def __init__(self, author: str, title: str, price: float):
        super().__init__(author, title, price)
        self.price = price + ((price * 30) / 100)


auth = input()
tit = input()
pri = float(input())

book = Book(auth, tit, pri)
golden_edition_book = GoldenEditionBook(auth, tit, pri)

print(book)
print(golden_edition_book)