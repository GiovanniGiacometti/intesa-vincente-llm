from abc import ABC, abstractmethod
from speech_recognition.audio import AudioData

from intesa_vincente_llm.enums import Language


class SpeechRecognizer(ABC):
    """
    Abstract class for speech recognizers.
    """

    def __init__(self, language: Language):
        self.language = language

    @abstractmethod
    def recognize(self, audio_data: AudioData, **kwargs) -> str:
        """
        Recognizes speech in the given audio data.

        :param audio_data: The audio data to recognize.
        :param kwargs: Additional keyword arguments.
        :return: The recognized speech.
        """
