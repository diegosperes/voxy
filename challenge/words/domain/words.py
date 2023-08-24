from typing import List, Tuple


def has_alpha_character(word: str) -> bool:
    """Check if a word has at least one alpha character."""
    for char in word:
        if char.isalpha():
            return True
    return False


def find_words_indexes(text: List[str]) -> List[Tuple[int, str]]:
    """Find the words with at least one alpha character."""
    return {index for index, word in enumerate(text) if has_alpha_character(word)}
