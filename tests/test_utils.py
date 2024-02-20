from app.utils import email_address_is_valid


def test_email_address_is_valid():
    """
    Test that email_address_is_valid correctly validate an email address
    """
    result = email_address_is_valid("test@mail.com")
    assert result == True
    result = email_address_is_valid("test-mail.com")
    assert result == False
