from enum import Enum


class BaseEnum(str, Enum):
    """
    Base class for enumerations.
    """


class Language(BaseEnum):
    """
    Enumeration of supported languages.
    """

    ENGLISH = "english"
    ITALIAN = "italian"

    def to_openai_string(self) -> str:
        """
        Converts the language to the string recognized by OpenAI API,
        which is the ISO 639-1 code.

        :return: The string representation of the language.
        """

        match self:
            case Language.ENGLISH:
                return "en"
            case Language.ITALIAN:
                return "it"
            case _:
                raise ValueError(f"Unsupported language: {self}")


class ImproveTranscriptionStrategy(BaseEnum):
    """
    Enumeration of strategies for improving the transcription.

    Attributes:
    -------------
    QUERY_LLM : str
        Query a language model for improving the transcription.
    PROMPT_WHISPER : str
        Give a prompt to the Whisper API for improving the transcription.
        This is not very useful in our case as words should not be too specific
        and in general we don't know what acronyms or abbreviations the user might use.
    """

    QUERY_LLM = "query_llm"
    PROMPT_WHISPER = "prompt_whisper"
