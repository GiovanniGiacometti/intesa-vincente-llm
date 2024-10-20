import logging
from io import BytesIO

from intesa_vincente_llm.enums import Language, ImproveTranscriptionStrategy
from intesa_vincente_llm.llm.factory import LLMFactory
from intesa_vincente_llm.llm.prompt_factory import PromptFactory
from intesa_vincente_llm.recognizer.base import SpeechRecognizer
from speech_recognition.audio import AudioData

from intesa_vincente_llm.utils.openai import OpenAIAPICaller


class WhisperAPIOpenAI(SpeechRecognizer, OpenAIAPICaller):
    """
    Speech recognizer using the OpenAI Whisper API.
    """

    def __init__(
        self,
        language: Language,
        improve_transcription_strategy: ImproveTranscriptionStrategy | None = None,
    ):
        """
        Initializes the recognizer with the language and strategy for improving the transcription.
        :param language: the language of the speech
        :param improve_transcription_strategy: the strategy for improving the transcription. If None, no strategy is used.
        """
        SpeechRecognizer.__init__(self, language)
        OpenAIAPICaller.__init__(self)
        self.improve_transcription_strategy = improve_transcription_strategy

    def recognize(self, audio_data: AudioData, **kwargs) -> str:
        """
        Recognizes speech in the given audio data.
        It queries the OpenAI Whisper API.

        :param audio_data: The audio data to recognize.
        :param kwargs: Additional arguments.
        :return: The recognized speech.
        """

        wav_data = BytesIO(audio_data.get_wav_data())
        wav_data.name = "audio.wav"

        transcript = self.client.audio.transcriptions.create(
            file=wav_data, model="whisper-1", language=self.language.to_openai_string()
        )

        logging.info(f"Original transcription: {transcript.text}")

        improved_transcription = self.improve_transcription(transcript.text)

        logging.info(f"Improved transcription: {improved_transcription}")

        return improved_transcription

    def improve_transcription(self, transcription: str) -> str:
        """
        Improves the transcription using the specified strategy.
        :param transcription: the original transcription
        :return: the improved transcription
        """
        if self.improve_transcription_strategy is None:
            return transcription

        match self.improve_transcription_strategy:
            case ImproveTranscriptionStrategy.QUERY_LLM:
                return self._improve_transcription_with_llm(transcription)
            case _:
                return transcription

    def _improve_transcription_with_llm(self, transcription: str) -> str:
        """
        Queries the language model to improve the transcription.
        :param transcription: the original transcription
        :return: the improved transcription
        """

        sys_prompt = PromptFactory.make_system_prompt_transcription_improving(
            self.language
        )

        # Keep a low temperature to avoid too creative responses
        llm = LLMFactory.make_openai_llm(sys_prompt=sys_prompt, temperature=0.0)

        return llm.query(prompt=transcription)
