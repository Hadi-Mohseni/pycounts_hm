from string import punctuation
from collections import Counter
from encodings.aliases import aliases


def load_text(input_file) -> str:
    """
    Load text from a text file and return as a string

    Parameters
    ----------
    input_file : str
        path to the file

    Returns
    -------
    str
        return the content of the file
    """
    with open(input_file, "r", encoding="utf_8") as file:
        text = file.read()
    return text


def clean_text(text: str) -> str:
    """
    remove all punctuation from given text.

    Parameters
    ----------
    text : str
        text to be cleaned

    Returns
    -------
    str
        cleaned text
    """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(input_file) -> dict:
    """
    count unique words in a string.

    Parameters
    ----------
    input_file : str
        file path or str

    Returns
    -------
    dict
        unique words as key and number of existence as value.
    """
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
