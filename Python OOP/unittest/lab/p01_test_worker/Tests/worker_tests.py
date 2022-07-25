"""
•	Test if the worker is initialized with the correct name, salary, and energy
•	Test if the worker's energy is incremented after the rest method is called
•	Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	Test if the worker's money is increased by his salary correctly after the work method is called
•	Test if the worker's energy is decreased after the work method is called
•	Test if the get_info method returns the proper string with correct values
"""
from test_worker import Worker

import unittest

class WorkerTests(unittest.TestCase):
    name = "Testio"
    salary = 100
    energy = 5
    # money = 0

    # class object initialization
    # def setUp(self) -> None:
    #     self.worker = Worker(self.name, self.salary, self.energy)

    # Test if the worker is initialized with the correct name, salary, and energy
    def test_init__when_name_salary_energy_are_valid__expect_to_create_worker(self):
        worker = Worker(self.name, self.salary, self.energy)
        self.assertEqual(worker.name, self.name)
        self.assertEqual(worker.salary, self.salary)
        self.assertEqual(worker.energy, self.energy)
        # self.assertEqual(worker.money, self.money)

    # Test if the worker's energy is incremented after the rest method is called
    def test_energy_increment__when_rest_method_is_called__expect_increase_with_one(self):
        worker = Worker(self.name, self.salary, self.energy)
        expected_energy = worker.energy + 1
        worker.rest()
        actual_energy = worker.energy
        self.assertEqual(expected_energy, actual_energy)

    # Test if an error is raised if the worker tries to work with negative energy or equal to 0
    def test_error_raise__when_worker_tries_to_work_with_zero_or_negative_energy__expect_exception(self):
        worker = Worker(self.name, self.salary, self.energy)
        worker.energy = 0
        with self.assertRaises(Exception) as context1:
            worker.work()

        worker.energy = -1
        with self.assertRaises(Exception) as context2:
            worker.work()

        self.assertEqual('Not enough energy.', str(context1.exception))
        self.assertEqual('Not enough energy.', str(context2.exception))

    # Test if the worker's money is increased by his salary correctly after the work method is called
    def test_money_increment__when_work_method_is_called__expect_increase_with_salary(self):
        worker = Worker(self.name, self.salary, self.energy)
        expected_money = worker.money + worker.salary * 2
        worker.work()
        worker.work()
        self.assertEqual(expected_money, worker.money)

    # Test if the worker's energy is decreased after the work method is called
    def test_energy_decrement__when_work_method_is_called__expect_decrease_with_one(self):
        worker = Worker(self.name, self.salary, self.energy)
        expected_energy = worker.energy - 1
        worker.work()
        actual_energy = worker.energy
        self.assertEqual(expected_energy, actual_energy)

    # Test if the get_info method returns the proper string with correct values
    def test_get_info_string__when_get_info_method_is_called__expect_valid(self):
        worker = Worker(self.name, self.salary, self.energy)
        valid_string = f'{worker.name} has saved {worker.money} money.'
        self.assertEqual(valid_string, worker.get_info())

if __name__ == "__main__":
    unittest.main()