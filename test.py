import time

import fire
import speech_recognition as sr
from dotenv import load_dotenv
import os

from speech_recognition import AudioData
import itertools


def combine_audio_chunks(audio_stream, chunks_to_combine=10):
    """
    Combines multiple AudioData chunks from a stream into larger chunks.

    Parameters:
        audio_stream: Iterator yielding AudioData instances
        chunks_to_combine: Number of chunks to combine into one

    Yields:
        AudioData: Combined audio data from multiple chunks
    """
    buffer = []

    # Use itertools.chain to handle the case when the last group is smaller
    for chunk in audio_stream:
        buffer.append(chunk)

        if len(buffer) >= chunks_to_combine:
            # Combine the raw audio data
            combined_data = b"".join(chunk.frame_data for chunk in buffer)

            # All chunks should have the same sample rate and width, so use the first chunk's values
            sample_rate = buffer[0].sample_rate
            sample_width = buffer[0].sample_width

            # Yield combined AudioData
            yield AudioData(combined_data, sample_rate, sample_width)
            buffer = []

    # Don't forget any remaining chunks
    if buffer:
        combined_data = b"".join(chunk.frame_data for chunk in buffer)
        yield AudioData(combined_data, buffer[0].sample_rate, buffer[0].sample_width)


def main():
    r = sr.Recognizer()

    # with sr.Microphone() as source:
    #     r.adjust_for_ambient_noise(source, duration=0.5)
    #
    #     print(source.SAMPLE_RATE, source.CHUNK)
    #
    # stop_listening = r.listen_in_background(source,
    #                         lambda _, chunk: print("You said: " + r.recognize_whisper_api(chunk, api_key=os.environ["OPENAI_API_KEY"])))
    #
    # print("Listening...")
    #
    # time.sleep(10)
    #
    # stop_listening(wait_for_stop=False)

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=0.5)
        source.CHUNK = 2048

        print(source.SAMPLE_RATE, source.CHUNK)

        # length of buffer is float(source.CHUNK) / source.SAMPLE_RATE

        print("Say something!")

        cur_audio = None

        for chunk in r.listen(source, stream=True):
            print("Got chunk")

            if cur_audio is None:
                print("Creating new audio chunk")
                cur_audio = chunk

            else:
                print("Adding to existing audio chunk")

                print("chunk length: " + str(len(chunk.frame_data)))
                print("current length: " + str(len(cur_audio.frame_data)))
                cur_audio.frame_data = b"".join([cur_audio.frame_data, chunk.frame_data])
                print("new length: " + str(len(cur_audio.frame_data)))

                # get duration of audio chunk

                # if duration is greater than 5 seconds, send to api

                duration = len(cur_audio.frame_data) / source.SAMPLE_RATE / cur_audio.sample_width
                print("Duration: " + str(duration))

                if duration > 1:
                    print("sending to api")
                    print("You said: " + r.recognize_whisper_api(cur_audio, api_key=os.environ["OPENAI_API_KEY"]))

                    cur_audio = None

        # Don't forget any remaining chunks
        if cur_audio is not None:

            print("You said: " + r.recognize_whisper_api(cur_audio, api_key=os.environ["OPENAI_API_KEY"]))


if __name__ == "__main__":
    load_dotenv()
    fire.Fire(main)
