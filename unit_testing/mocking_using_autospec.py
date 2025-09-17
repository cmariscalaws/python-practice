import unittest
from unittest.mock import create_autospec

# A simple class to be mocked
class DatabaseClient:
    def get_user(self, user_id):
        pass


def test_get_user():
    """
        autospec=True

        By default, mocks are very permissive and will accept any arguments,
        even misspelled ones. Using autospec=True (or spec=True) configures the mock
        to match the interface of the real object.
        This helps prevent subtle bugs caused by typos.
    """

    # Create a mock with autospec=True
    mock_client = create_autospec(DatabaseClient)

    # Correct call: no error
    mock_client.get_user(123)

    # Incorrect call: raises a TypeError
    try:
        mock_client.get_user(user_id=123, extra_arg='value')
    except TypeError as e:
        print(f"Caught expected error: {e}")

if __name__ == '__main__':
    test_get_user()
