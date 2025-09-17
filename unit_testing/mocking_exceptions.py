from unittest.mock import MagicMock

def process_data(client):
    try:
        client.connect()
        # ... processing logic ...
    except ConnectionError as e:
        return f"Error: {str(e)}"


def test_process_data():
    '''
    In your code, mock_client is an instance of MagicMock,
        which is a flexible mock object provided by Python's unittest.mock library.
        MagicMock does not need to "know" about the real client class or its connect method in advance.

    Here's how it works:
        When you create mock_client = MagicMock(), it can dynamically pretend to have any attribute or method.
        When you set mock_client.connect.side_effect = ConnectionError(...),
            you are telling the mock that whenever its connect method is called, it should raise a ConnectionError.

        In process_data, you call client.connect(). Since you pass mock_client as the client argument,
            this calls mock_client.connect(), which triggers the side_effect and raises the exception.

    MagicMock does not require any prior knowledge of the real client or its connect method.
        It simply creates attributes and methods as needed when you access them.
        This makes it very flexible for mocking objects in tests.
    '''


    # Create a mock that raises a ConnectionError when connect is called
    mock_client = MagicMock()
    mock_client.connect.side_effect = ConnectionError("Unable to connect to the server.")

    # Test the process_data function with the mock
    result = process_data(mock_client)
    print(result)  # Output: Error: Unable to connect to the server.
    assert result == "Error: Unable to connect to the server.", f"Unexpected result: {result}"

if __name__ == '__main__':
    test_process_data()