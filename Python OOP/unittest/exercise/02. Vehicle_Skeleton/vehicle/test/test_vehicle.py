import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):

    def test_init(self):
        sample_object = Vehicle(45.67, 123.567)
        self.assertEqual(sample_object.fuel, 45.67)
        self.assertEqual(sample_object.capacity, 45.67)
        self.assertEqual(sample_object.horse_power, 123.567)
        self.assertEqual(sample_object.fuel_consumption, sample_object.DEFAULT_FUEL_CONSUMPTION)

    def test_drive(self):
        sample_object = Vehicle(45.67, 123.567)
        kilometers = 100
        fuel_needed = sample_object.DEFAULT_FUEL_CONSUMPTION * kilometers

        self.assertEqual()

