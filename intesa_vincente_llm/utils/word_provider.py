import os
import random
from intesa_vincente_llm.enums import Language
import json


class WordProvider:
    FOLDER_NAME = "words"

    @classmethod
    def get_word_to_guess(cls, language: Language) -> str:
        """
        Load a list of words for a given language.
        """

        match language:
            case Language.ENGLISH:
                path = os.path.join(cls.FOLDER_NAME, "english.json")
            case Language.ITALIAN:
                path = os.path.join(cls.FOLDER_NAME, "italian.json")
            case _:
                raise ValueError(f"Unsupported language: {language}")

        with open(path, "r") as file:
            words = json.load(file)

        return random.choice(words)
