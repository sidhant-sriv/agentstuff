import re
from llama_index.core.tools import FunctionTool




def count_x_in_text(x: str, text: str) -> int:
    """Counts the number of times x appears in the text."""
    return text.lower().count(x.lower())


def starts_with(text: str, prefix: str) -> bool:
    """Check if the text starts with a specific prefix."""
    return text.startswith(prefix)


def ends_with(text: str, suffix: str) -> bool:
    """Check if the text ends with a specific suffix."""
    return text.endswith(suffix)


def split_text(text: str, delimiter: str = " ") -> list:
    """Split text into a list of words based on a delimiter."""
    return text.split(delimiter)


def join_text(words: list, delimiter: str = " ") -> str:
    """Join a list of words into a string with a specified delimiter."""
    return delimiter.join(words)


def to_uppercase(text: str) -> str:
    """Convert all characters in the text to uppercase."""
    return text.upper()


def to_lowercase(text: str) -> str:
    """Convert all characters in the text to lowercase."""
    return text.lower()


def capitalize_text(text: str) -> str:
    """Capitalize the first character of the text."""
    return text.capitalize()


def title_case(text: str) -> str:
    """Convert text to title case."""
    return text.title()


def strip_whitespace(text: str) -> str:
    """Remove leading and trailing whitespace."""
    return text.strip()


def contains_substring(text: str, substring: str) -> bool:
    """Check if a substring exists within the text."""
    return substring in text


def reverse_text(text: str) -> str:
    """Reverse the order of characters in the text."""
    return text[::-1]


def find_all_regex(text: str, pattern: str) -> list:
    """Find and extract all substrings matching a regular expression."""
    return re.findall(pattern, text)


def count_words(text: str) -> int:
    """Count the number of words in the text."""
    return len(text.split())


def text_operations() -> list:
    """Perform multiple text operations."""
    return [
        count_x_in_text,
        starts_with,
        ends_with,
        contains_substring,
        count_words,
    ]


def return_text_operations() -> list:
    """Return the text functions."""
    return [FunctionTool.from_defaults(fn=func) for func in text_operations()]