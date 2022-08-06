# from project.movie_specification.movie import Movie


class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        username = f"Username: {self.username}, Age: {self.age}"
        if self.movies_liked:
            liked = "\n".join([x.details() for x in self.movies_liked])
        else:
            liked = "No movies liked."
        if self.movies_owned:
            owned = "\n".join([x.details() for x in self.movies_owned])
        else:
            owned = "No movies owned."

        return "\n".join([username, "Liked movies:", liked, "Owned movies:", owned])

