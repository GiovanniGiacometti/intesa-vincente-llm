from abc import ABC, abstractmethod


class LLM(ABC):
    def __init__(self, sys_prompt: str | None, temperature: float):
        self.sys_prompt = sys_prompt
        self.temperature = temperature

    @abstractmethod
    def query(self, prompt: str, **kwargs) -> str:
        """
        Queries the language model with the given prompt and returns the response.
        :param prompt: user prompt to the language model
        :return:
        """
