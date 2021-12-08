import unittest
from book_examples import get_formatted_name


class NamingSchemeTests(unittest.TestCase):

    # initiate the instance, as a constructor
    def setUp(self) -> None:
        # create my own class instance ...
        pass

    def test_one(self):
        name = get_formatted_name('kurt', 'cobain')
        self.assertEqual(name, "Kurt Cobain")
    def test_second(self):
        surname = get_formatted_name("dave", "grohl")
        self.assertEqual("Dave Grohl", surname)


if __name__ == "__main__":
    unittest.main()