import re

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


def email_address_is_valid(email: str) -> bool:
    """
    Return True if email address format is valid, else False
    """
    if re.fullmatch(regex, email):
        return True
    else:
        return False
