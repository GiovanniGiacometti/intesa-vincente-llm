from intesa_vincente_llm.enums import Language


class PromptFactory:
    @staticmethod
    def make_system_prompt_transcription_improving(
        language: Language,
    ) -> str:
        """
        Create a system prompt for improving the transcription.
        """

        match language:
            case Language.ENGLISH:
                return """
                       You will receive a transcription of a speech. The text will be composed by a list of words
                       that were pronunciated by the speaker. Your task is to correct the transcription by 
                       fixing spelling mistakes. You should only change the words that you are 100% sure
                       that are wrong. If you are not sure about a word, you must leave it as it is.
                       Don't add anything else in your response, your output should be equal to the input,
                       apart from the corrections.
                       """
            case Language.ITALIAN:
                return """
                       Riceverai una trascrizione di un discorso. Il testo sarà composto da una lista di parole
                       che sono state pronunciate dallo speaker. Il tuo compito è correggere la trascrizione
                       correggendo gli errori di ortografia. Dovresti cambiare solo le parole di cui sei sicuro al 100%
                       che sono sbagliate. Se non sei sicuro di una parola, devi lasciarla com'è.
                       Non aggiungere altro nella tua risposta, il tuo output dovrebbe essere uguale all'input,
                       a parte le correzioni.
                        """
            case _:
                raise ValueError(f"Unsupported language: {language}")

    @staticmethod
    def make_prompt_for_word_guessing_instruction(
        language: Language
    ) -> str:
        """
        Create a system prompt to instruct the llm to guess a word.
        """

        match language:
            case Language.ENGLISH:
                return """
                       You will receive a list of words. These words taken together should
                       make you think of a single word. Your task is to guess the word.
                       Your answer must be that single word, nothing else.
                       """
            case Language.ITALIAN:
                return """
                        Riceverai una lista di parole. Queste parole prese insieme dovrebbero
                        farti pensare a una singola parola. Il tuo compito è indovinare la parola.
                        La tua risposta deve essere quella singola parola, niente altro.
                       """
            case _:
                raise ValueError(f"Unsupported language: {language}")
