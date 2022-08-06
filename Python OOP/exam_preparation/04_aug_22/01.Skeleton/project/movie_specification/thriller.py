from project.movie_specification.movie import Movie


class Thriller(Movie):
    DEFAULT_AGE_RESTRICTION = 16

    def __init__(self, title, year, owner, age_restriction=DEFAULT_AGE_RESTRICTION):
        # if age_restriction < self.DEFAULT_AGE_RESTRICTION:
        #     raise ValueError("Thriller movies must be restricted for audience under 16 years!")
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 16:
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")
        self.__age_restriction = value
