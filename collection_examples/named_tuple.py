# collection_examples/named_tuple.py

from collections import namedtuple

# Define a named tuple type called 'Point'
Point = namedtuple('Point', ['x', 'y'])

def test_point():
    p = Point(5, 7)
    print(f'x: {p.x}, y: {p.y}')
    assert p.x == 5
    assert p.y == 7
    print("test_point passed.")

if __name__ == "__main__":
    test_point()