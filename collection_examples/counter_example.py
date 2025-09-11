# file: tests/test_counter_example.py
from collections import Counter

class TestCounterExample():
    def test_counter_from_list(self):
        data = ['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']
        expected = Counter({'B': 5, 'A': 3, 'C': 2})
        print(f"counter_from_list: {Counter(data)}")
        assert Counter(data) == expected

    def test_counter_from_dict(self):
        data = {'A': 3, 'B': 5, 'C': 2}
        expected = Counter({'A': 3, 'B': 5, 'C': 2})
        print(f"counter_from_dict: {Counter(data)}")
        assert Counter(data) == expected

    def test_counter_from_kwargs(self):
        expected = Counter({'A': 3, 'B': 5, 'C': 2})
        print(f"counter_kwargs: {Counter(A=3, B=5, C=2)}")
        assert Counter(A=3, B=5, C=2) == expected

if __name__ == '__main__':
    test = TestCounterExample()
    test.test_counter_from_list()
    test.test_counter_from_dict()
    test.test_counter_from_kwargs()
    print("All tests passed.")