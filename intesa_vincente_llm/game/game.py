import logging

from intesa_vincente_llm.enums import Language, ImproveTranscriptionStrategy
import questionary

from intesa_vincente_llm.listener.factory import ListenerFactory
from intesa_vincente_llm.llm.factory import LLMFactory
from intesa_vincente_llm.llm.prompt_factory import PromptFactory
from intesa_vincente_llm.recognizer.factory import SpeechRecognizerFactory


class IntesaVincente:
    @classmethod
    def play(cls):
        # 1. Ask the user to choose a language

        language = cls._ask_language()

        # 2. Print the word that the llm will try to guess

        secret_word = cls._get_word_to_guess(language)

        logging.info(
            f"The word that the llm will try to guess is: {secret_word}"
        )

        # 3. Initialize the listener and listen

        logging.info(
            f"Get ready to speak!"
        )

        listener = ListenerFactory.make_microphone_listener()
        audio_data = listener.listen()

        # 4. Initialize the recognizer and recognize the speech

        recognizer = SpeechRecognizerFactory.make_openai_speech_recognizer(
            language=language,
            improve_transcription_strategy=ImproveTranscriptionStrategy.QUERY_LLM,
        )

        transcribed_text = recognizer.recognize(audio_data)

        logging.info(f"Transcribed text: {transcribed_text}")

        # 5. Let the LLM guess the word

        sys_prompt = PromptFactory.make_prompt_for_word_guessing_instruction(
            language=language
        )

        llm = LLMFactory.make_openai_llm(sys_prompt=sys_prompt, temperature=0.4)

        llm_guess = llm.query(transcribed_text)

        logging.info(f"The LLM guessed: {llm_guess}")

        # 6. Evaluate the guess

        if llm_guess.lower() == secret_word.lower():
            logging.info("Congratulations! The llm guessed the word!")
        else:
            logging.info("Sorry, the llm failed!")

    @staticmethod
    def _ask_language() -> Language:
        language = questionary.select(
            "What language do you speak? / Quale lingua parli?", choices=list(Language)
        ).ask()

        return Language(language.lower())

    @staticmethod
    def _get_word_to_guess(language: Language) -> str:
        match language:
            case Language.ENGLISH:
                return "table"
            case Language.ITALIAN:
                return "tavolo"
            case _:
                raise ValueError(f"Unsupported language: {language}")