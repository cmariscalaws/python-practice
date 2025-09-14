from typing import List

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def isSubsequence(s: str, t: str) -> bool:
    s_ptr = 0
    t_ptr = 0

    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        t_ptr += 1

    return s_ptr == len(s)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    result1 = isSubsequence(s, t)
    assert result1 == True, f"Expected {True}, but got {result1}"

    s = "axc"
    t = "ahbgdc"
    result2 = isSubsequence(s, t)
    assert result2 == False, f"Expected {False}, but got {result2}"

    s = "aaaaaa"
    t = "bbaaaa"
    result3 = isSubsequence(s, t)
    assert result3 == False, f"Expected {False}, but got {result3}"


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
