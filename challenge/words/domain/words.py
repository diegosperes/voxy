import string
import functools
import unicodedata

from typing import Any, Iterable, List, Set, Union


class State:
    def __init__(
        self,
        next_states: List[str],
        values: Set[Any] = None,
        final: bool = False,
    ):
        self.final = final
        self.acceptable_values = values if values else set()
        self.next_states = next_states


class EnglishLanguage:
    states = {
        "initial": State(["alpha"]),
        "hiphen": State(["alpha"], values=set("-")),
        "contraction": State(["alpha"], values=set("'")),
        "acronym": State(["alpha"], values=set("."), final=True),
        "punctuation": State([], values=set(",:;!?"), final=True),
        "alpha": State(
            ["alpha", "hiphen", "punctuation", "contraction", "acronym"],
            values=set(string.ascii_lowercase),
            final=True,
        ),
    }

    @staticmethod
    def normalise_value(value: Any) -> str:
        if (
            (value.startswith("(") and value.endswith(")"))
            or (value.startswith('"') and value.endswith('"'))
            or (value.startswith("`") and value.endswith("`"))
        ):
            value = value[1 : len(value) - 1]

        return (
            unicodedata.normalize("NFKD", value)
            .encode("ASCII", "ignore")
            .decode()
            .lower()
        )

    @classmethod
    def get_next_state(cls, character: Any, state: State) -> Union[State, None]:
        for state_name in state.next_states:
            next_state = cls.states[state_name]
            if character in next_state.acceptable_values:
                return next_state


# TODO: Validate single letter words
class WordStateMachine:
    @functools.lru_cache(maxsize=1000)
    def validate(self, value: Iterable, language: EnglishLanguage) -> bool:
        current_state = language.states["initial"]

        for character in language.normalise_value(value):
            if current_state is None:
                break

            current_state = language.get_next_state(character, current_state)

        return current_state is not None and current_state.final


def find_word_indexes(text: List[str], language: EnglishLanguage) -> Set[int]:
    """Find the words with at least one alpha character."""
    machine = WordStateMachine()
    return {
        index for index, word in enumerate(text) if machine.validate(word, language)
    }
