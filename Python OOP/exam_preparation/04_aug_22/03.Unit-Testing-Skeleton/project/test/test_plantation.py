import unittest
from project.plantation import Plantation
from sys import maxsize


class TestPlantation(unittest.TestCase):

    def test_init(self):
        sample_object = Plantation(5)
        self.assertEqual(sample_object.size, 5)
        self.assertEqual(sample_object.plants, {})
        self.assertEqual(sample_object.workers, [])

    def test_size_validation(self):
        with self.assertRaises(ValueError) as cc:
            sample_object = Plantation(-1)
        self.assertEqual(str(cc.exception), "Size must be positive number!")
        with self.assertRaises(ValueError) as cc:
            sample_object = Plantation(-maxsize)
        self.assertEqual(str(cc.exception), "Size must be positive number!")

    def test_hire_worker(self):
        sample_object = Plantation(5)
        sample_object.hire_worker("Nazo")
        sample_object.hire_worker("Mazo")
        self.assertEqual(sample_object.workers[0], "Nazo")
        self.assertEqual(sample_object.workers[1], "Mazo")
        self.assertEqual("Avocato successfully hired.", sample_object.hire_worker("Avocato"))
        with self.assertRaises(ValueError) as cc:
            sample_object.hire_worker("Nazo")
        self.assertEqual(str(cc.exception), "Worker already hired!")

    def test_len_method(self):
        sample_object = Plantation(5)
        self.assertEqual(0, len(sample_object))
        sample_object.plants = {"Nazo": [None] * 8}
        self.assertEqual(8, len(sample_object))

    def test_planting(self):
        sample_object = Plantation(3)
        with self.assertRaises(ValueError) as cc:
            sample_object.planting("Nazo", "Rose")
        self.assertEqual(str(cc.exception), "Worker with name Nazo is not hired!")
        sample_object.hire_worker("Nazo")
        sample_object.hire_worker("Avocato")
        self.assertEqual("Nazo planted it's first Dahlia.", sample_object.planting("Nazo", "Dahlia"))
        self.assertEqual("Nazo planted Rose.", sample_object.planting("Nazo", "Rose"))
        sample_object.planting("Avocato", "Tree")
        with self.assertRaises(ValueError) as cc2:
            sample_object.planting("Avocato", "Tulip")
        self.assertEqual(str(cc2.exception), "The plantation is full!")

    def test_str_method(self):
        sample_object = Plantation(3)
        self.assertEqual(str(sample_object), "Plantation size: 3\n")
        sample_object.hire_worker("Nazo")
        sample_object.hire_worker("Avocato")
        sample_object.planting("Nazo", "Rose")
        sample_object.planting("Avocato", "Tulip")
        self.assertEqual(str(sample_object),
                         "Plantation size: 3" + "\n"
                         "Nazo, Avocato" + "\n"
                         "Nazo planted: Rose" + "\n"
                         "Avocato planted: Tulip")

    def test_repr_method(self):
        sample_object = Plantation(3)
        self.assertEqual(repr(sample_object).strip(), "Size: 3\nWorkers:")
        sample_object.hire_worker("Nazo")
        sample_object.hire_worker("Avocato")
        sample_object.planting("Nazo", "Rose")
        sample_object.planting("Avocato", "Tulip")
        self.assertEqual(repr(sample_object),
                         "Size: 3" + "\n"
                         "Workers: Nazo, Avocato"
                         )

