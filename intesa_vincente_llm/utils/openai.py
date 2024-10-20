import os
from openai import OpenAI


class OpenAIAPICaller:
    """
    Mixin class for OpenAI API clients.
    It could be implemented as a singleton, but it's not necessary for this simple use case.
    """

    def __init__(self):
        """
        Initializes the OpenAI API client
        """
        self._client: OpenAI | None = None

    @property
    def client(self) -> OpenAI:
        if self._client is None:
            self._client = OpenAI(api_key=self.load_key())
        return self._client

    @staticmethod
    def load_key() -> str:
        if "OPENAI_API_KEY" not in os.environ:
            raise ValueError(
                "Set environment variable OPENAI_API_KEY to enable OpenAI API."
            )

        return os.environ["OPENAI_API_KEY"]
