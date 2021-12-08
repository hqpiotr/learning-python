import unittest
from book_examples import get_formatted_name


class TestUserNames(unittest.TestCase):
    def test_wtf(self):
        name = get_formatted_name("amadeus", "mozart")
        self.assertEqual(name, "Amadeus Mozart")


if __name__ == "__main__":
    unittest.main()
