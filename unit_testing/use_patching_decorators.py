from urllib import request

'''
unittest.mock is a powerful Python library for replacing parts of your system under test with mock objects.
    This isolates your test code from external dependencies, ensuring that tests are fast,
    predictable, and focused on a single unit of work.

The most common ways to use unittest.mock are:
patch(): Replaces objects, functions, or classes in a module with a mock.
MagicMock: Creates a versatile mock object that can simulate a wide range of behaviors.

Core concepts
The patch() function
    patch() is the primary tool for replacing objects during a test. It can be used as a decorator,
     a context manager, or by manually calling start() and stop().
Patching decorators:
    This is the most common approach for a clean, scoped replacement.
    The patched object is passed as an argument to the decorated test function.
'''
def get_status_code(url):
    with request.urlopen(url) as response:
        return response.status

#test
from unittest.mock import patch, MagicMock
import unittest

class TestGetStatusCode(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_get_status_code(self, mock_urlopen):
        # mock the response object to have a status attribute
        # mock is overriding the enter() method of the context manager
        mock_response = MagicMock()
        mock_response.__enter__.return_value.status = 200
        mock_urlopen.return_value = mock_response

        # execute the function with a test URL
        url = 'http://example.com'
        result = get_status_code(url)

        # assert the status code is as expected
        self.assertEqual(result, 200)
        # ensure urlopen was called with the correct URL
        mock_urlopen.assert_called_once_with(url)

if __name__ == "__main__":
    unittest.main()
