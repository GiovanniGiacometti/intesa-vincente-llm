from intesa_vincente_llm.llm.base import LLM

from intesa_vincente_llm.utils.openai import OpenAIAPICaller


class OpenAILLM(LLM, OpenAIAPICaller):
    def __init__(
        self,
        sys_prompt: str | None = None,
        model_name: str = "gpt-4o-mini",
        temperature: float = 0.2,
    ):
        """
        Initializes the OpenAI language model.
        :param sys_prompt: the system prompt to prepend to the user prompt
        :param model_name: the name of the OpenAI language model
        :param temperature: the temperature parameter for the language model
        """
        LLM.__init__(self, sys_prompt=sys_prompt, temperature=temperature)
        OpenAIAPICaller.__init__(self)
        self.model_name = model_name

    def query(self, prompt: str, **kwargs) -> str:
        """
        Queries the OpenAI language model with the given prompt and returns the response.
        :param prompt:
        :return: LLM response
        """

        messages = []
        if self.sys_prompt is not None:
            messages.append({"role": "system", "content": self.sys_prompt})

        messages.append({"role": "user", "content": prompt})

        chat_completion = self.client.chat.completions.create(
            messages=messages,  # type: ignore
            model=self.model_name,
            temperature=self.temperature,
        )

        response = chat_completion.choices[0].message.content

        if response is None:
            raise ValueError("Received None respone")

        return response
