def is_subsequence(subsequence: str, sequence: str) -> bool:
    """
    Determines if 'subsequence' is a subsequence of 'sequence'.
    A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

    Args:
        subsequence (str): The string to check as a potential subsequence.
        sequence (str): The string to check against.

    Returns:
        bool: True if 'subsequence' is a subsequence of 'sequence', False otherwise.
    """
    # Pointer for subsequence
    subseq_index = 0
    # Pointer for sequence
    seq_index = 0

    # Iterate while both pointers are within their respective string lengths
    while subseq_index < len(subsequence) and seq_index < len(sequence):
        # If characters match, move subsequence pointer forward
        if subsequence[subseq_index] == sequence[seq_index]:
            subseq_index += 1
        # Always move sequence pointer forward
        seq_index += 1

    # If we've matched all characters in subsequence, it's a subsequence
    return subseq_index == len(subsequence)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Test case 1: subsequence exists
    print("Running Test Case 1: subsequence exists")
    s = "abc"
    t = "ahbgdc"
    expected1 = True
    print(f"Input subsequence: {s}")
    print(f"Input sequence: {t}")
    print(f"Expected: {expected1}")
    result1 = is_subsequence(s, t)
    print(f"Result: {result1}")
    assert result1 == expected1, f"Expected {expected1}, but got {result1}"
    print("Test Case 1 Passed\n")

    # Test case 2: subsequence does not exist
    print("Running Test Case 2: subsequence does not exist")
    s = "axc"
    t = "ahbgdc"
    expected2 = False
    print(f"Input subsequence: {s}")
    print(f"Input sequence: {t}")
    print(f"Expected: {expected2}")
    result2 = is_subsequence(s, t)
    print(f"Result: {result2}")
    assert result2 == expected2, f"Expected {expected2}, but got {result2}"
    print("Test Case 2 Passed\n")

    # Test case 3: repeated characters, not a subsequence
    print("Running Test Case 3: repeated characters, not a subsequence")
    s = "aaaaaa"
    t = "bbaaaa"
    expected3 = False
    print(f"Input subsequence: {s}")
    print(f"Input sequence: {t}")
    print(f"Expected: {expected3}")
    result3 = is_subsequence(s, t)
    print(f"Result: {result3}")
    assert result3 == expected3, f"Expected {expected3}, but got {result3}"
    print("Test Case 3 Passed\n")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
