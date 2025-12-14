import unittest
from unittest.mock import patch

from utils.validation import validate_number, validate_positive


class TestValidationUtils(unittest.TestCase):

    # ---------- validate_number ----------

    @patch("utils.validation.st.error")
    def test_validate_number_correct(self, mock_error):
        value = validate_number("100000", "ventas")
        self.assertEqual(value, 100000.0)
        mock_error.assert_not_called()

    @patch("utils.validation.st.error")
    def test_validate_number_none(self, mock_error):
        value = validate_number(None, "ventas")
        self.assertIsNone(value)
        mock_error.assert_called_once()

    @patch("utils.validation.st.error")
    def test_validate_number_invalid_string(self, mock_error):
        value = validate_number("abc", "ventas")
        self.assertIsNone(value)
        mock_error.assert_called_once()

    # ---------- validate_positive ----------

    @patch("utils.validation.st.error")
    def test_validate_positive_correct(self, mock_error):
        value = validate_positive(50000.0, "utilidad")
        self.assertEqual(value, 50000.0)
        mock_error.assert_not_called()

    @patch("utils.validation.st.error")
    def test_validate_positive_zero(self, mock_error):
        value = validate_positive(0.0, "utilidad")
        self.assertEqual(value, 0.0)
        mock_error.assert_not_called()

    @patch("utils.validation.st.error")
    def test_validate_positive_negative(self, mock_error):
        value = validate_positive(-100.0, "utilidad")
        self.assertIsNone(value)
        mock_error.assert_called_once()


if __name__ == "__main__":
    unittest.main()
