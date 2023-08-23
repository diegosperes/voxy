import pytest

from words.domain.alpha_words import find_alpha_words_indexes, has_alpha_character


@pytest.mark.parametrize(
    "character,expected",
    [
        pytest.param("1", False, id="single-number"),
        pytest.param("@", False, id="special-character"),
        pytest.param("↑", False, id="single-unicode-symbol"),
        pytest.param("a", True, id="single-alpha-character"),
        pytest.param("@bout", True, id="word-with-special-character"),
        pytest.param("about", True, id="alpha-word"),
        pytest.param("h1", True, id="word-with-number"),
        pytest.param("ç", True, id="accented-word"),
    ],
)
def test_has_alpha_character(character: str, expected: bool):
    assert has_alpha_character(character) == expected


def test_get_alpha_words():
    text = "  Tonight @peres ! Drink \"cachaça\" and throw your 2 hands up ↑ in the sky!  "
    assert find_alpha_words_indexes(text.split()) == {0, 1, 3, 4, 5, 6, 7, 9, 10, 12, 13, 14}
