class Category:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def edit(self, new_name):
        self.__name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
