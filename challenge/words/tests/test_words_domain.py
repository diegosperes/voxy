import pytest

from words.domain.words import find_words_indexes, WordStateMachine, EnglishLanguage


@pytest.mark.parametrize(
    "character,expected",
    [
        pytest.param("1", False, id="single-number"),
        pytest.param("@", False, id="special-character"),
        pytest.param("↑", False, id="single-unicode-symbol"),
        pytest.param("@bout", False, id="word-with-special-character"),
        pytest.param("h1", False, id="word-with-number"),
        pytest.param("year2023", False, id="word-alphanumeric"),
        pytest.param("co,ma", False, id="comma-between-word"),
        pytest.param("excla!mation", False, id="exclamation-between-word"),
        pytest.param("ques?tion", False, id="question-between-word"),
        pytest.param("semi;colon", False, id="semicolon-between-word"),
        pytest.param("col:on", False, id="colon-between-word"),
        pytest.param("a", True, id="single-alpha-character"),
        pytest.param("about", True, id="word"),
        pytest.param("Paradise", True, id="word-upper-case"),
        pytest.param("comma,", True, id="word-ending-with-comma"),
        pytest.param("exclamation!", True, id="word-ending-with-exclamation"),
        pytest.param("question?", True, id="word-ending-with-question"),
        pytest.param("semicolon;", True, id="word-ending-with-semicolon"),
        pytest.param("colon:", True, id="word-ending-with-colon"),
        pytest.param("period.", True, id="word-ending-with-period"),
        pytest.param("cachaça", True, id="accented-word"),
        pytest.param("ice-cream", True, id="hyphen-word"),
        pytest.param("B.O.G.O.", True, id="acronym-word"),
        pytest.param("we'll", True, id="word-contraction"),
        pytest.param('"double-quotes"', True, id="word-within-double-quotes"),
        pytest.param("(parentheses)", True, id="word-within-rounded-parentheses"),
        pytest.param("`rounded-parentheses`", True, id="word-within-grave"),
    ],
)
def test_word_state_machine(character: str, expected: bool):
    machine = WordStateMachine()
    assert machine.validate(character, EnglishLanguage) == expected


def test_find_words_indexeswords():
    expected = {0, 3, 4, 5, 6, 7, 9, 10, 12, 13, 14}
    text = "Tonight @peres ! Drink cachaça and throw your 2 hands up ↑ in the sky!"
    assert find_words_indexes(text.split(), EnglishLanguage) == expected


def test_find_words_indexeswords_benchmark(benchmark):
    text = "Tonight @peres ! Drink cachaça and throw your 2 hands up ↑ in the sky!"
    word_indexes = benchmark(find_words_indexes, text.split(), EnglishLanguage)
    assert len(word_indexes) == 11
