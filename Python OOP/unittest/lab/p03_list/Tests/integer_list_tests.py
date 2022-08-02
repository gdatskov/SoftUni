from integer_list import IntegerList

import unittest


class IntegerListTests(unittest.TestCase):

    # __init__ should only take integers, and store them
    def test_init__should_take_only_integers_and_store_them__expect_valid_storage(self):
        argument_sample = [1, "2", 3, None, 4, True, 5]

        test_init_list = IntegerList(*argument_sample)

        self.assertEqual([1, 3, 4, 5], test_init_list.get_data())

    # add operation, should add an element and returns the list.
    # If the element is not an integer, a ValueError is thrown
    def test_add__when_adding__expect_to_return_the_list_or_throw_value_error_if_invalid_entry(self):
        test_integer_list = IntegerList()
        lis = [1]
        invalid_values = ["aug_22", None, True, False]

        self.assertEqual(lis, test_integer_list.add(1))

        for inv_val in invalid_values:
            with self.assertRaises(ValueError) as value_error_context:
                test_integer_list.add(inv_val)
            self.assertEqual("Element is not Integer", str(value_error_context.exception))

    # test remove_index operation removes the element on that index and returns it.
    # If the index is out of range, an IndexError is thrown
    def test_remove_index__when_removing__expect_to_return_the_element_on_index_or_throw_error_if_out_of_range(self):
        sample_list = [1, 2, 3]
        valid_idx = 1
        invalid_idx = 3
        test_integer_list = IntegerList(*sample_list)

        del sample_list[valid_idx]
        test_integer_list.remove_index(valid_idx)

        self.assertEqual(sample_list, test_integer_list.get_data())

        with self.assertRaises(IndexError) as context:
            test_integer_list.remove_index(invalid_idx)
        self.assertEqual("Index is out of range", str(context.exception))

    # test get should return the specific element
    # If the index is out of range, an IndexError is thrown
    def test_get_should_return_specific_element__when_index_is_out_of_range__expect_index_error(self):
        sample_list = [1, 2, 3]
        valid_idx = 1
        invalid_idx = 3
        test_integer_list = IntegerList(*sample_list)

        expected_element = sample_list[valid_idx]
        actual_element = test_integer_list.get(valid_idx)

        self.assertEqual(expected_element, actual_element)

        with self.assertRaises(IndexError) as context:
            test_integer_list.get(invalid_idx)
        self.assertEqual("Index is out of range", str(context.exception))

    # test insert
    # If the index is out of range, IndexError is thrown
    # If the element is not an integer, ValueError is thrown
    def test_insert_element_at_given_position__when_inserted__expect_valid_placement_or_index_err_or_value_err(self):
        sample_args = [1, 2, 3]
        valid_idx = len(sample_args) - 1
        invalid_idx = len(sample_args)
        invalid_values = ["aug_22", None, True, False]
        sample_value = sample_args[-1] + 1
        expected_list = [1, 2, sample_value, 3]
        test_sample = IntegerList(*sample_args)

        for inv_val in invalid_values:
            with self.assertRaises(ValueError) as value_error_context:
                test_sample.insert(valid_idx, inv_val)
            self.assertEqual("Element is not Integer", str(value_error_context.exception))

        with self.assertRaises(IndexError) as index_error_context:
            test_sample.insert(invalid_idx, sample_value)
        self.assertEqual("Index is out of range", str(index_error_context.exception))

        test_sample.insert(valid_idx, sample_value)
        self.assertEqual(expected_list, test_sample.get_data())

    # test get_biggest
    def test_get_biggest__when_get_biggest_is_called__expect_highest_value_returned(self):
        sample_args = [-5, 0, 2, 5]
        test_sample = IntegerList(*sample_args)

        biggest = test_sample.get_biggest()

        self.assertEqual(biggest, 5)

    # test get_index
    def test_get_index__when_get_index_is_called__expect_to_return_correct_index(self):
        sample_args = [0, 1, 2]
        test_sample = IntegerList(*sample_args)
        expected_value = 2

        actual_value_at_idx = test_sample.get_index(expected_value)

        self.assertEqual(expected_value, actual_value_at_idx)


if __name__ == "__main__":
    unittest.main()
