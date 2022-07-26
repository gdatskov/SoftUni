"""

"""
from test_cat import Cat

import unittest


class CatTests(unittest.TestCase):
    test_cat_name = "Testio"
    test_cat_is_fed = False
    test_cat_is_sleepy = False
    test_cat_size = 0

    # class object initialization
    # def setUp(self) -> None:
    #     self.worker = Worker(self.name, self.salary, self.energy)

    # Test Cat's size is increased after eating
    def test_cat_size__when_cat_eat_increase_size__expect_increase_plus_one(self):
        cat = Cat(self.test_cat_name)
        cat.fed = False
        cat.size = 10
        expected_size = cat.size + 1
        cat.eat()
        self.assertEqual(expected_size, cat.size)

    # Test Cat is fed after eating
    def test_cat_is_fed__when_cat_eat__expect_cat_is_fed(self):
        cat = Cat(self.test_cat_name)
        cat.fed = False
        cat.eat()
        self.assertEqual(cat.fed, True)

    # Cat cannot eat if already fed, raises an error
    def test_cat_cannot_eat__when_cat_is_fed__expect_exception(self):
        cat = Cat(self.test_cat_name)
        cat.fed = True
        with self.assertRaises(Exception) as context:
            cat.eat()
        self.assertEqual('Already fed.', str(context.exception))

    # Cat cannot fall asleep if not fed, raises an error
    def test_cat_sleep__when_cat_is_not_fed__expect_exception(self):
        cat = Cat(self.test_cat_name)
        cat.fed = False
        with self.assertRaises(Exception) as context:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(context.exception))

    # Cat is not sleepy after sleeping
    def test_cat_is_not_sleepy__when_cat_have_slept__expect_not_sleepy(self):
        cat = Cat(self.test_cat_name)
        cat.sleepy = True
        cat.fed = True
        cat.sleep()
        self.assertEqual(cat.sleepy, False)


if __name__ == "__main__":
    unittest.main()
