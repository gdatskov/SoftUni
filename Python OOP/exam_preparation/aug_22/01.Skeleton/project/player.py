class Player:
    INITIAL_STAMINA = 100
    MAX_STAMINA = 100
    __players_list = []

    def __init__(self, name, age, stamina=INITIAL_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    @property
    def need_sustenance(self):
        return True if self.stamina < 100 else False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        if value in self.__players_list:
            raise Exception(f"Name {value} is already used!")
        self.__players_list.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

# a = Player("pesho", 12)
# # a.name = "gosho"
# a.stamina = 11
# print(a)
# print(a.name)
# print(a.need_sustenance)
# #
# b = Player("pesho", 13)
# print(b)
# print(b.name)
