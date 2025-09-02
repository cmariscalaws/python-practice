from typing import List


class MapExamples(object):
    """
    The map function in Python applies a given function to each item of an iterable (such as a list) and returns an iterator of the results.

    Parameters:
        function: A function to apply to each element of the iterable.
        iterable: An iterable (e.g., list, tuple) whose elements will be processed.

    Returns:
        An iterator that yields the results of applying the function to each element of the iterable.

    Example:
        map(lambda x: x * 2, [1, 2, 3]) produces an iterator yielding 2, 4, 6.
        To get a list, use list(map(lambda x: x * 2, [1, 2, 3])) which returns [2, 4, 6].
    """
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    """
        Returns a list where each number in self.numbers is squared.

        Uses the built-in map function to apply a lambda (anonymous function)
        that squares each element (x ** 2) in the input list.
        
        x is the parameter representing each element from self.numbers as map iterates over the list.
        The expression x ** 2 computes the square of x.
        So, for every number in the input list, x takes its value and returns its square. There is only one parameter (x) in this lambda function.

        Example:
            If self.numbers = [1, 2, 3], returns [1, 4, 9].
    """
    def square(self) -> List[int]:
        return list(map(lambda x: x ** 2, self.numbers))



if __name__ == '__main__':

    numbers = [1, 2, 3, 4, 5]
    map_examples = MapExamples(numbers)
    squared_numbers = map_examples.square()

    assert squared_numbers == [1, 4, 9, 16, 25], f"Expected [1, 4, 9, 16, 25], but got {squared_numbers}"

    print("Original numbers:", numbers)
    print("Squared numbers:", squared_numbers)