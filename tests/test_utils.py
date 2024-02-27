import unittest

from app.utils import email_address_is_valid, send_email


class TestUtils(unittest.TestCase):
    def test_email_address_is_valid(self):
        """
        Test that email_address_is_valid correctly validate an email address
        """
        result = email_address_is_valid("test@mail.com")
        self.assertEqual(result, True)
        result = email_address_is_valid("test-mail.com")
        self.assertEqual(result, False)

    def test_send_email_bad_email(self):
        """
        Test that send_email raise ValueError if the email address is bad
        """
        with self.assertRaises(ValueError):
            send_email("bad-mail.com", "subject_test", "body_test")
