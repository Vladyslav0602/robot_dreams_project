import io
import sys
import unittest
from unittest.mock import patch
from phonebook import add, list


class TestPhoneBook(unittest.TestCase):
    @patch('builtins.input', side_effect=["John", "1234567890"])
    def test_add(self, mock_input):
        test_contacts = []
        add(test_contacts)
        self.assertEqual(len(test_contacts), 1)
        self.assertEqual(test_contacts[0]["name"], "John")
        self.assertEqual(test_contacts[0]["phone"], "1234567890")

    def test_list(self):
        test_contacts = [
            {"name": "Alice", "phone": "1111111111"},
            {"name": "Bob", "phone": "2222222222"}
        ]
        captured_output = io.StringIO()
        sys.stdout = captured_output

        list(test_contacts)

        sys.stdout = sys.__stdout__  # Reset redirection

        output = captured_output.getvalue()
        self.assertIn("Alice", output)
        self.assertIn("Bob", output)
        self.assertIn("1111111111", output)
        self.assertIn("2222222222", output)


if __name__ == "__main__":
    unittest.main()
