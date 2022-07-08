from project.animal import Animal


class Lion(Animal):
    def __init__(self,  name, gender, age):
        super(Lion, self).__init__(name, gender, age, 50)
