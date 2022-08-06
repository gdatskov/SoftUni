import unittest
from project.plantation import Plantation


class TestPlantation(unittest.TestCase):

    def test_init(self):
        sample_object = Plantation(5)
        self.assertEqual(sample_object.size, 5)
        self.assertEqual(sample_object.plants, {})
        self.assertEqual(sample_object.workers, [])

    def test_size_validation(self):
        with self.assertRaises(ValueError) as cc:
            sample_object = Plantation(-1)
        self.assertEqual(cc, "Size must be positive number!")