class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level
        # self.class_name = self.__class__.__name__

    # def get_class_name(self):
    #     return self.__class__.__name__

    def __str__(self):
        # return f"{self.username} of type {self.get_class_name()} has level {self.level}"
        return f"{self.username} of type {self.__class__.__name__} has level {self.level}"
