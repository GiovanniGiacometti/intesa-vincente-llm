from intesa_vincente_llm.listener.microphone_listener import MicrophoneSpeechRecognition


class ListenerFactory:
    @staticmethod
    def make_microphone_listener(**kwargs) -> MicrophoneSpeechRecognition:
        """
        Factory method for creating a microphone listener.
        :return: MicrophoneSpeechRecognition object
        """
        return MicrophoneSpeechRecognition()
