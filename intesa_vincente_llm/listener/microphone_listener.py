import logging

from speech_recognition import AudioData, Microphone, Recognizer


class MicrophoneSpeechRecognition:
    """
    Simple wrapper for the speech recognition library
    """

    @staticmethod
    def listen(
        chunk_size: int = 1024,
        sample_rate: int | None = None,
        device_index: int | None = None,
        wait_for_ambient_noise_adjustment: int | None = None,
    ) -> AudioData:
        """
        Listens to the microphone and returns the audio data

        :param chunk_size: the size of the audio chunks
        :param sample_rate: the sample rate of the audio
        :param device_index: the index of the audio device
        :param wait_for_ambient_noise_adjustment: the duration to wait for ambient noise adjustment
        :return: the audio data
        """
        r = Recognizer()

        with Microphone(
            chunk_size=chunk_size, sample_rate=sample_rate, device_index=device_index
        ) as source:
            if wait_for_ambient_noise_adjustment is not None:
                logging.info("Calibrating noise...")

                r.adjust_for_ambient_noise(
                    source, duration=wait_for_ambient_noise_adjustment
                )

            logging.info("Speak!")

            audio = r.listen(source)

            logging.info("Audio received!")

            return audio
