"""
_Module to give implementations of some string-related methods.
DO NOT CHANGE THIS FILE_
"""


def word_count(sentence: str) -> int:
    """_Function to check the number of words._
    Args:
        _sentence_ (str): _A given sentence_

    Returns:
        _int_: _Returns the word count in string._
    """
    words = len(sentence.split())
    print(words)
    return words


def char_count(sentence: str) -> int:
    """_Function to check the number of characters._
    Args:
        _sentence_ (str): _A given sentence_

    Returns:
        _int_: _Returns the character count in string._
    """
    chars = len(sentence)
    print(chars)
    return chars


def first_char(sentence: str) -> str:
    """_Function to check the first character using the string index._
    Args:
        _sentence_ (str): _A given sentence_

    Returns:
        _str_: _Returns the first character in string._
    """
    first = sentence[0]
    return first


def last_char(sentence: str) -> str:
    """_Function to check the last character using the string index._
    Args:
        _sentence_ (str): _A given sentence_

    Returns:
        _str_: _Returns the last character in string._
    """
    last = sentence[-1]
    return last
