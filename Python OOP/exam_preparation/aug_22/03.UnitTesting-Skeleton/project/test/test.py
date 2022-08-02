from project.movie import Movie
import unittest

class TestsMovie(unittest.TestCase):
    sample_name = "Pirates of the Carribean"
    sample_year = 2003
    sample_rating = 8.1
    sample_actors = ["Johnny Depp", "Keira Knightley"]

    def test_init(self):
        sample_object = Movie(self.sample_name, self.sample_year, self.sample_rating)
        self.assertEqual(sample_object.name, self.sample_name)
        self.assertEqual(sample_object.year, self.sample_year)
        self.assertEqual(sample_object.rating, self.sample_rating)
        # self.assertEqual(sample_object.actors, [])

    def test_name_setter(self):
        sample_object = Movie(self.sample_name, self.sample_year, self.sample_rating)
        with self.assertRaises(ValueError) as context:
            sample_object.name = ""
        self.assertEqual(str(context.exception), "Name cannot be an empty string!")

    def test_year_setter(self):
        sample_object = Movie(self.sample_name, self.sample_year, self.sample_rating)
        with self.assertRaises(ValueError) as context:
            sample_object.year = 1886
        self.assertEqual(str(context.exception), "Year is not valid!")

    def test_add_actor(self):
        sample_object = Movie(self.sample_name, self.sample_year, self.sample_rating)

        self.assertEqual(sample_object.actors, [])

        sample_object.add_actor(self.sample_actors[0])
        sample_object.add_actor(self.sample_actors[1])

        self.assertEqual(sample_object.actors, self.sample_actors)

        self.assertEqual(
            f"{self.sample_actors[0]} is already added in the list of actors!",
            sample_object.add_actor(self.sample_actors[0]))

        self.assertEqual(
            f"{self.sample_actors[1]} is already added in the list of actors!",
            sample_object.add_actor(self.sample_actors[1]))

    def test_rating_greater_than(self):
        sample_object = Movie(self.sample_name, self.sample_year, self.sample_rating)
        another_sample_object = Movie("Star Trek", 1966, 8.4)
        other_sample_object = Movie("X", 2022, 6.1)
        self.assertEqual(sample_object > other_sample_object,
            f'"{self.sample_name}" is better than "{other_sample_object.name}"')
        self.assertEqual(sample_object > another_sample_object,
                         f'"{another_sample_object.name}" is better than "{self.sample_name}"')

    def test_repr(self):
        sample_object = Movie(self.sample_name, self.sample_year, self.sample_rating)
        [sample_object.add_actor(actor) for actor in self.sample_actors]
        self.assertEqual(
            repr(sample_object),
            f"Name: {sample_object.name}\nYear of Release: {sample_object.year}\n"
            f"Rating: {sample_object.rating:.2f}\nCast: {', '.join(sample_object.actors)}"
            )
