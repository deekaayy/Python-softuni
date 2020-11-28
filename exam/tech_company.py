from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def __init__(self, id, os, price: float):
        self.id = str(id)
        self.os = str(os)
        self.price = float(price)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        if not value.isalpha():
            raise Exception("Invalid id!")
        elif len(value) < 8:
            raise Exception("Invalid id!")
        self.__id = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Invalid price!")
        self.__price = value


class Phone(Item):
    def __init__(self, id, os, price,):
        Item.__init__(self, id, os, price)

    def make_call(self):
        print("Making call...")

    def receive_call(self):
        print("Receiving call!")

    def send_message(self):
        print("Sending message...")

    def receive_message(self):
        print("Receiving a message!")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        if not value.isalpha():
            raise Exception("Invalid id!")
        elif len(value) < 8:
            raise Exception("Invalid id!")
        self._id = value

class CellPhone(Phone):
    def __init__(self, id, os, price):
        super().__init__(id, os, price)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        if not value.isalpha():
            raise Exception("Invalid id!")
        elif len(value) < 8:
            raise Exception("Invalid id!")
        self.__id = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Invalid price!")
        self.__price = value


class Tablet(Item):
    def __init__(self, id, os, price):
        Item.__init__(self, id, os, price)

    def stream_movie(self):
        print("Streaming_movie...")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        if not value.isalpha():
            raise Exception("Invalid id!")
        elif len(value) < 8:
            raise Exception("Invalid id!")
        self.__id = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Invalid price!")
        self.__price = value


class SmartPhone(Phone):
    def __init__(self, id, os, price, apps_list:[]):
        super().__init__(id, os, price)
        self.apps_list = apps_list

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        if not value.isalpha():
            raise Exception("Invalid id!")
        elif len(value) < 8:
            raise Exception("Invalid id!")
        self.__id = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception("Invalid price!")
        self.__price = value

    @property
    def apps_list(self):
        return self.__apps_list

    @apps_list.setter
    def apps_list(self, value):
        if len(value) < 5:
            raise Exception("Invalid number of applications!" )
        self.__apps_list = value


data = input()
data_list = []

while not data == "end":
    try:
        item = eval(data)
        data_list.append(item)
    except Exception as ex:
        print(ex)

    data = input()

data = input().split()
while not data[0] == "end":
    try:
        if data[0] == "test":
            if any(x.id == data[1] for x in data_list):
                item = list(filter(lambda item: item.id == data[1], data_list))[0]
                if data[1] in item.__dict__:
                    item.data[1]
                else:
                    raise Exception("Invalid request has been made")

    except Exception as ex:
        print(ex)