import fire
import speech_recognition as sr
from dotenv import load_dotenv
import os


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)

        print("Say something!")
        audio = r.listen(source)

        print("You said: " + r.recognize_whisper_api(audio, api_key=os.environ["OPENAI_API_KEY"]))  # type: ignore


if __name__ == "__main__":
    load_dotenv()
    fire.Fire(main)
