import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def test_init(self):
        sample_object = Mammal("Mamut", "Prehistoric", "Moooo")
        self.assertEqual(sample_object.name, "Mamut")
        self.assertEqual(sample_object.type, "Prehistoric")
        self.assertEqual(sample_object.sound, "Moooo")
        # self.assertEqual(sample_object.get_kingdom(), "animals")

    def test_make_sound(self):
        sample_object = Mammal("Mamut", "Prehistoric", "Moooo")
        self.assertEqual(sample_object.make_sound(), "Mamut makes Moooo")

    def test_get_kingdom(self):
        sample_object = Mammal("Mamut", "Prehistoric", "Moooo")
        self.assertEqual(sample_object.get_kingdom(), "animals")

    def test_info(self):
        sample_object = Mammal("Mamut", "Prehistoric", "Moooo")
        self.assertEqual(sample_object.info(), "Mamut is of type Prehistoric")

