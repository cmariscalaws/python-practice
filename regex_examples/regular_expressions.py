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
"""
import re

def is_valid_email(email):
    """
    Checks if the input string is a valid email address.
    Pattern: one or more word chars, @, one or more word chars, ., 2-4 word chars
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,4}$"
    return bool(re.match(pattern, email))

def extract_numbers(text):
    """
    Extracts all integer numbers from the input string.
    Pattern: one or more digits
    """
    pattern = r"\d+"
    return re.findall(pattern, text)

def has_date(text):
    """
    Checks if the input string contains a date in format YYYY-MM-DD.
    Pattern: 4 digits, dash, 2 digits, dash, 2 digits
    """
    pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    return bool(re.search(pattern, text))

def split_words(text):
    """
    Splits a string into words using whitespace and punctuation as delimiters.
    Pattern: split on non-word characters
    """
    pattern = r"\W+"
    return [w for w in re.split(pattern, text) if w]

def extract_hashtags(text):
    """
    Extracts hashtags from a string (words starting with #).
    Pattern: # followed by word characters
    """
    pattern = r"#\w+"
    return re.findall(pattern, text)

def contains_url(text):
    """
    Checks if the input string contains a URL (http or https).
    Pattern: http(s):// followed by non-whitespace characters
    """
    pattern = r"https?://\S+"
    return bool(re.search(pattern, text))

def extract_word_after_indicator(text, indicator):
    """
    Extracts the first word or token immediately following a given indicator in the input string.
    Pattern: indicator (case-insensitive), optional whitespace, then a token (sequence of non-whitespace, non-comma characters)
    Returns the token if found, else None.
    Example: extract_word_after_indicator("group type: admin", "group type:") -> "admin"
    Example: extract_word_after_indicator("role: manager", "role:") -> "manager"
    Example: extract_word_after_indicator("group type: admin-user", "group type:") -> "admin-user"
    Example: extract_word_after_indicator("group type: ", "group type:") -> None
    """
    pattern = rf"{re.escape(indicator)}\s*([^\s,]+)"
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1) if match else None

def extract_phone_numbers(text):
    """
    Extracts all phone numbers in formats like (123) 456-7890, 123-456-7890, 123.456.7890, 1234567890.
    """
    pattern = r"(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}"
    return re.findall(pattern, text)

def extract_dates(text):
    """
    Extracts dates in formats YYYY-MM-DD, MM/DD/YYYY, DD.MM.YYYY.
    """
    pattern = r"\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}\.\d{2}\.\d{4})\b"
    return re.findall(pattern, text)

def is_valid_ip(ip):
    """
    Validates if the input string is a valid IPv4 address (each octet 0-255).
    """
    pattern = r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
    return bool(re.match(pattern, ip))

def find_mentions(text):
    """
    Finds all @mentions in the text (e.g., @username).
    """
    pattern = r"@\w+"
    return re.findall(pattern, text)

def replace_digits(text, char):
    """
    Replaces all digits in the text with the given character.
    """
    pattern = r"\d"
    return re.sub(pattern, char, text)

def split_by_delimiters(text):
    """
    Splits text by comma, semicolon, or pipe.
    """
    pattern = r"[,;|]"
    return [t.strip() for t in re.split(pattern, text) if t.strip()]

def is_strong_password(password):
    """
    Validates password strength: at least one uppercase, one lowercase, one digit, one special char, min 8 chars.
    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,}$"
    return bool(re.match(pattern, password))

def extract_quoted_strings(text):
    """
    Extracts all quoted strings (single or double quotes).
    """
    pattern = r"(['\"])(.*?)(\1)"
    return [m[1] for m in re.findall(pattern, text)]

def find_repeated_words(text):
    """
    Finds all repeated words (case-insensitive).
    """
    pattern = r"\b(\w+)\b(?=.*\b\1\b)"
    return list(set(re.findall(pattern, text, re.IGNORECASE)))

def find_words_of_length(text, length):
    """
    Finds all words of a specific length.
    """
    pattern = rf"\b\w{{{length}}}\b"
    return re.findall(pattern, text)

def extract_domain_from_email(email):
    """
    Extracts domain from an email address.
    """
    pattern = r"@([\w\.-]+)"
    match = re.search(pattern, email)
    return match.group(1) if match else None

def is_valid_hex_color(text):
    """
    Validates hex color code (#RGB, #RRGGBB).
    """
    pattern = r"^#(?:[0-9a-fA-F]{3}){1,2}$"
    return bool(re.match(pattern, text))

def extract_sentences(text):
    """
    Extracts sentences ending with ., !, or ?
    """
    pattern = r"[^.!?]+[.!?]"
    return [s.strip() for s in re.findall(pattern, text)]

def find_non_ascii(text):
    """
    Finds all non-ASCII characters in the text (returns each character separately).
    """
    pattern = r"[^\x00-\x7F]"
    return re.findall(pattern, text)

def remove_extra_spaces(text):
    """
    Removes extra spaces from the text (leaves single spaces).
    """
    pattern = r"\s+"
    return re.sub(pattern, " ", text).strip()

if __name__ == "__main__":
    # Test is_valid_email
    assert is_valid_email("test@example.com")
    assert is_valid_email("user.name@domain.co")
    assert not is_valid_email("invalid-email@com")
    assert not is_valid_email("@missingusername.com")

    # Test extract_numbers
    assert extract_numbers("There are 12 apples and 34 oranges.") == ["12", "34"]
    assert extract_numbers("No numbers here!") == []

    # Test has_date
    assert has_date("Today's date is 2025-09-20.")
    assert not has_date("No date here.")

    # Test split_words
    assert split_words("Hello, world! How are you?") == ["Hello", "world", "How", "are", "you"]
    assert split_words("") == []

    # Test extract_hashtags
    assert extract_hashtags("#python is #awesome!") == ["#python", "#awesome"]
    assert extract_hashtags("No hashtags here.") == []

    # Test contains_url
    assert contains_url("Visit https://github.com for code.")
    assert contains_url("Try http://example.com now!")
    assert not contains_url("No links here.")

    # Test extract_word_after_indicator
    assert extract_word_after_indicator("group type: admin", "group type:") == "admin"
    assert extract_word_after_indicator("role: manager", "role:") == "manager"
    assert extract_word_after_indicator("group type: admin-user", "group type:") == "admin-user"
    assert extract_word_after_indicator("group type: ", "group type:") is None
    assert extract_word_after_indicator("no group type here", "group type:") is None
    assert extract_word_after_indicator("group type: admin, group type: user", "group type:") == "admin"
    assert extract_word_after_indicator("group type: admin-user, group type: user", "group type:") == "admin-user"# Only first occurrence, special chars in word

    # Test extract_phone_numbers
    assert extract_phone_numbers("Call me at (123) 456-7890 or 987-654-3210.") == ["(123) 456-7890", "987-654-3210"]
    assert extract_phone_numbers("Numbers: 1234567890, 123.456.7890") == ["1234567890", "123.456.7890"]
    assert extract_phone_numbers("No phone here.") == []

    # Test extract_dates
    assert extract_dates("Dates: 2025-09-20, 09/20/2025, 20.09.2025") == ["2025-09-20", "09/20/2025", "20.09.2025"]
    assert extract_dates("No date.") == []

    # Test is_valid_ip
    assert is_valid_ip("192.168.1.1")
    assert is_valid_ip("8.8.8.8")
    assert not is_valid_ip("999.999.999.999")
    assert not is_valid_ip("abc.def.ghi.jkl")

    # Test find_mentions
    assert find_mentions("Hi @user and @admin!") == ["@user", "@admin"]
    assert find_mentions("No mentions.") == []

    # Test replace_digits
    assert replace_digits("abc123def456", "*") == "abc***def***"
    assert replace_digits("no digits", "*") == "no digits"

    # Test split_by_delimiters
    assert split_by_delimiters("a,b;c|d") == ["a", "b", "c", "d"]
    assert split_by_delimiters("one|two") == ["one", "two"]

    # Test is_strong_password
    assert is_strong_password("Abcdef1!")
    assert not is_strong_password("abcdefg")
    assert not is_strong_password("ABCDEFG1")
    assert not is_strong_password("Abcdefgh")

    # Test extract_quoted_strings
    assert extract_quoted_strings('He said "hello" and then \'bye\'.') == ["hello", "bye"]
    assert extract_quoted_strings("No quotes here.") == []

    # Test find_repeated_words
    assert set(find_repeated_words("cat dog cat bird dog")) == {"cat", "dog"}
    assert find_repeated_words("one two three") == []

    # Test find_words_of_length
    assert find_words_of_length("one two three four five", 3) == ["one", "two"]
    assert find_words_of_length("hello world", 5) == ["hello", "world"]

    # Test extract_domain_from_email
    assert extract_domain_from_email("test@example.com") == "example.com"
    assert extract_domain_from_email("user@sub.domain.co") == "sub.domain.co"
    assert extract_domain_from_email("invalid-email") is None

    # Test is_valid_hex_color
    assert is_valid_hex_color("#fff")
    assert is_valid_hex_color("#123abc")
    assert not is_valid_hex_color("#1234")
    assert not is_valid_hex_color("123abc")

    # Test extract_sentences
    assert extract_sentences("Hello! How are you? I am fine.") == ["Hello!", "How are you?", "I am fine."]
    assert extract_sentences("No sentence") == []

    # Test remove_extra_spaces
    assert remove_extra_spaces("This   is   spaced   out.") == "This is spaced out."
    assert remove_extra_spaces("  Leading and trailing   ") == "Leading and trailing"

    print("All tests passed.")
