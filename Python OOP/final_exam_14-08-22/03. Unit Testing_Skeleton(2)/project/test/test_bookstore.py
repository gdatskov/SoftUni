import unittest

from project.bookstore import Bookstore


class BookstoreTest(unittest.TestCase):

    def test_init(self):
        sample_object = Bookstore(3)
        self.assertEqual(sample_object.books_limit, 3)
        self.assertEqual(sample_object.availability_in_store_by_book_titles, {})
        self.assertEqual(sample_object.total_sold_books, 0)
        with self.assertRaises(ValueError) as cc1:
            sample_object2 = Bookstore(0)
        self.assertEqual(str(cc1.exception), f"Books limit of 0 is not valid")
        with self.assertRaises(ValueError) as cc2:
            sample_object3 = Bookstore(-12345)
        self.assertEqual(str(cc2.exception), f"Books limit of -12345 is not valid")

    def test_len_method(self):
        sample_object = Bookstore(3)
        self.assertEqual(len(sample_object), 0)

        sample_object.receive_book("Testbook", 3)
        self.assertEqual(len(sample_object), 3)

    def test_receive_book(self):
        sample_object = Bookstore(6)
        with self.assertRaises(Exception) as cc:
            sample_object.receive_book("Testbook", 7)
        self.assertEqual(str(cc.exception), "Books limit is reached. Cannot receive more books!")

        self.assertEqual(
            sample_object.receive_book("Testbook", 3),
            "3 copies of Testbook are available in the bookstore."
        )
        self.assertEqual(
            sample_object.receive_book("Testbook", 3),
            "6 copies of Testbook are available in the bookstore."
        )

        self.assertEqual(sample_object.availability_in_store_by_book_titles, {"Testbook": 6})

    def test_sell_book(self):
        sample_object = Bookstore(3)

        with self.assertRaises(Exception) as cc:
            sample_object.sell_book("Testbook", 3)
        self.assertEqual(str(cc.exception), "Book Testbook doesn't exist!")

        sample_object.receive_book("Testbook", 3)
        with self.assertRaises(Exception) as cc:
            sample_object.sell_book("Testbook", 4)
        self.assertEqual(str(cc.exception), "Testbook has not enough copies to sell. Left: 3")

        self.assertEqual(sample_object.sell_book("Testbook", 3), "Sold 3 copies of Testbook")

        sample_object.receive_book("OtherBook", 2)
        self.assertEqual(sample_object.sell_book("OtherBook", 2), "Sold 2 copies of OtherBook")

    def test_str_method(self):
        sample_object = Bookstore(5)
        sample_object.receive_book("Testbook", 3)
        sample_object.receive_book("Otherbook", 2)
        sample_object.sell_book("Otherbook", 1)
        self.assertEqual(str(sample_object),
                         "Total sold books: 1\n"
                         "Current availability: 4\n"
                         " - Testbook: 3 copies\n"
                         " - Otherbook: 1 copies"
                         )


if __name__ == "__main__":
    main()