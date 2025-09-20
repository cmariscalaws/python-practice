"""
regular_expressions.py

This module demonstrates common use cases for Python's re (regular expression) library.
Each example includes a docstring explaining the pattern, a function implementing the regex,
and test cases with assertions to verify correctness.

Guidance:
- Use raw strings (r'...') for regex patterns to avoid escaping backslashes.
- Use re.match for matching from the start, re.search for searching anywhere, and re.findall for extracting all matches.
- Use grouping (parentheses) to capture parts of the match.
- Use character classes ([abc]), quantifiers (*, +, ?), and anchors (^, $) for flexible patterns.

Regex Cheat Sheet:
------------------
.        Any character except newline
\w      Word character [a-zA-Z0-9_]
\W      Non-word character
\d      Digit [0-9]
\D      Non-digit
\s      Whitespace (space, tab, newline)
\S      Non-whitespace
^        Start of string
$        End of string
*        0 or more repetitions
+        1 or more repetitions
?        0 or 1 repetition (optional)
{m,n}    Between m and n repetitions
[]       Character class (set of characters)
[^...]   Negated character class
|        Alternation (OR)
()       Grouping/capturing
\b      Word boundary
\A      Start of string
\Z      End of string

Examples:
- r"\d+" matches one or more digits (e.g. "123", "42")
- r"^abc" matches 'abc' at the start of a string (e.g. "abcde")
- r"abc$" matches 'abc' at the end of a string (e.g. "xyzabc")
- r"cat|dog" matches 'cat' or 'dog' (e.g. "I have a cat.", "I have a dog.")
- r"[A-Z]{2,4}" matches 2 to 4 uppercase letters (e.g. "USA", "HTML")
- r"[aeiou]" matches any vowel (e.g. "apple")
- r"[^0-9]+" matches one or more non-digit characters (e.g. "abc!@#")
- r"colou?r" matches 'color' or 'colour' (optional 'u')
- r"\w*" matches zero or more word characters (e.g. "hello", "")
- r"\s+" matches one or more whitespace characters (e.g. "   ", "\t\n")
- r"(\d{3})-(\d{2})-(\d{4})" matches and captures a SSN like "123-45-6789"
- r"\bword\b" matches 'word' as a whole word (not as part of 'sword')
- r"\Astart" matches 'start' at the beginning of the string
- r"end\Z" matches 'end' at the end of the string

Key Functions in the re module:
re.match(pattern, string, flags=0): Checks for a match only at the beginning of the string. Returns a Match object if found, None otherwise. 
re.search(pattern, string, flags=0): Searches for the first occurrence of the pattern anywhere in the string. Returns a Match object if found, None otherwise.
re.findall(pattern, string, flags=0): Finds all non-overlapping matches of the pattern and returns them as a list of strings (or tuples if groups are used).
re.sub(pattern, repl, string, count=0, flags=0): Replaces occurrences of the pattern in the string with repl.
re.split(pattern, string, maxsplit=0, flags=0): Splits the string by occurrences of the pattern.
re.compile(pattern, flags=0): Compiles a regular expression into a pattern object for more efficient repeated use.
"""
import re

def extract_product_codes(text):
    pass

def extract_info_usernames(log):
    pass

if __name__ == "__main__":
    # Test scenario #1
    # You have a string containing a list of product codes, some of which are in the format ABC-1234 (three uppercase letters, a dash, and four digits).
    # Write a regular expression to extract all valid product codes from the string.
    text = "Order: ABC-1234, xyz-5678, DEF-9876, GHI-0001, invalid, JKL-12, MNO-34567"
    expected = ["ABC-1234", "DEF-9876", "GHI-0001"]
    assert extract_product_codes(text) == expected

    # Test scenario #2
    # You have a log file containing lines like:
    log = '''
    [2025-09-20 14:23:01] INFO: User john_doe logged in
    [2025-09-20 14:24:15] ERROR: Failed login for user jane99
    [2025-09-20 14:25:00] INFO: User alice logged out
    [2025-09-20 14:26:00] INFO: User bob123 performed action
    '''
    expected = ["john_doe", "alice", "bob123"]
    assert extract_info_usernames(log) == expected

    print("All tests passed.")
