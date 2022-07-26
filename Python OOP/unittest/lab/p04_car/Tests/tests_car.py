from car_car import Car

import unittest


class CarTests(unittest.TestCase):
    sample_make = "Ford"
    sample_model = "Shit"
    sample_fuel_consumption = 1000
    sample_fuel_capacity = 5000
    sample_fuel_amount = 0

    def test_init(self):
        sample = Car(self.sample_make, self.sample_model, self.sample_fuel_consumption, self.sample_fuel_capacity)
        self.assertEqual(sample.make, self.sample_make)
        self.assertEqual(sample.model, self.sample_model)
        self.assertEqual(sample.fuel_consumption, self.sample_fuel_consumption)
        self.assertEqual(sample.fuel_capacity, self.sample_fuel_capacity)
        self.assertEqual(sample.fuel_amount, self.sample_fuel_amount)

    def test_make_setter(self):
        sample = Car(self.sample_make, self.sample_model, self.sample_fuel_consumption, self.sample_fuel_capacity)
        invalid_values = [None, ""]
        # invalid_values.extend([True, False])

        for inv_val in invalid_values:
            with self.assertRaises(Exception) as context:
                sample.make = inv_val
            self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_model_setter(self):
        sample = Car(self.sample_make, self.sample_model, self.sample_fuel_consumption, self.sample_fuel_capacity)
        invalid_values = [None, ""]

        for inv_val in invalid_values:
            with self.assertRaises(Exception) as context:
                sample.model = inv_val
            self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_fuel_consumption_setter(self):
        sample = Car(self.sample_make, self.sample_model, self.sample_fuel_consumption, self.sample_fuel_capacity)
        invalid_values = [0, -1]

        for inv_val in invalid_values:
            with self.assertRaises(Exception) as context:
                sample.fuel_consumption = inv_val
            self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_fuel_capacity_setter(self):
        sample = Car(self.sample_make, self.sample_model, self.sample_fuel_consumption, self.sample_fuel_capacity)
        invalid_values = [0, -1]

        for inv_val in invalid_values:
            with self.assertRaises(Exception) as context:
                sample.fuel_capacity = inv_val
            self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_fuel_amount_setter(self):
        sample = Car(self.sample_make, self.sample_model, self.sample_fuel_consumption, self.sample_fuel_capacity)

        with self.assertRaises(Exception) as context:
            sample.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    def test_refuel(self):
        sample = Car(self.sample_make, self.sample_model, self.sample_fuel_consumption, self.sample_fuel_capacity)
        invalid_values = [0, -1]

        for inv_val in invalid_values:
            with self.assertRaises(Exception) as context:
                sample.refuel(inv_val)
            self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_drive(self):
        sample = Car(self.sample_make, self.sample_model, self.sample_fuel_consumption, self.sample_fuel_capacity)

        sample.fuel_amount = sample.fuel_capacity
        with self.assertRaises(Exception) as context:
            sample.drive(sample.fuel_amount / sample.fuel_consumption * 100 + 0.000000001)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))


if __name__ == "__main__":
    unittest.main()
