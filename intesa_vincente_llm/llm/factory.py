from intesa_vincente_llm.llm.openai import OpenAILLM


class LLMFactory:
    @staticmethod
    def make_openai_llm(**kwargs) -> OpenAILLM:
        """
        Create a new OpenAI language model.
        """

        return OpenAILLM(**kwargs)
