import fire
from dotenv import load_dotenv

from intesa_vincente_llm.game.game import IntesaVincente
from intesa_vincente_llm.utils.logging import setup_logging
import logging


def main():
    logging.info("The game is about to start!")

    game = IntesaVincente()
    game.play()

    logging.info("The game has ended!")


if __name__ == "__main__":
    load_dotenv()
    setup_logging()
    fire.Fire(main)
