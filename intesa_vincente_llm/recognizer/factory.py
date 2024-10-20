from intesa_vincente_llm.enums import Language
from intesa_vincente_llm.recognizer.base import SpeechRecognizer
from intesa_vincente_llm.recognizer.whisper_openai import WhisperAPIOpenAI


class SpeechRecognizerFactory:
    @staticmethod
    def make_openai_speech_recognizer(language: Language, **kwargs) -> SpeechRecognizer:
        """
        Create a speech recognizer object. Right now, it returns
        the WhisperAPIOpenAI class, as it's the only one available.
        :param language:
        :return: the Speech Recognizer object
        """

        return WhisperAPIOpenAI(language=language, **kwargs)
