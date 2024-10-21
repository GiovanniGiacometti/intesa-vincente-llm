# Intesa Vincente, with LLM

Have you ever been excited to play ["Intesa Vincente"](https://it.wikipedia.org/wiki/Reazione_a_catena_-_L%27intesa_vincente) 
but found yourself one player short? Good news! This dilemma has been resolved. 
Now you can enjoy the game with just you, a friend, and an AI language model filling in as the third player.

## Game explanation

"Reazione a Catena" (Chain Reaction) is a popular Italian television game show. "Intesa Vincente" (Winning Understanding) is one of the challenges within the show.
In "Intesa Vincente," two contestants from the same team must work together to help their third teammate guess a specific word. The rules are as follows:

- The two team members giving clues can only use single words as hints.
- They are not allowed to use gestures, sounds, or any form of non-verbal communication.
- The words they use as clues cannot be derivatives or variations of the target word.
- They must alternate in giving clues.

The goal is to guess as many words as possible within a set time limit, usually 60 seconds.

## Instructions

First, you need to clone the repository to a folder that suits you. 

Then, you should create a virtual enviroment and install the requirements.

I'm using `uv` as package manager. If you also want to use it, you can install it following the [guide](https://docs.astral.sh/uv/getting-started/installation/).

Then, you can run the following commands:

```bash
make create-env
make sync
```

and the environment will be created along with the dependencies installed. 

Otherwise, you can create the environment and install the dependencies using any other dependency manager and the provided
`requirements.txt` file.

As a last step, you need to get an OpenAI API key. You can get one [here](https://platform.openai.com/api-keys). Then, you can copy
the `.env.example` file to a `.env` file and paste your API key there.

You are finally ready to play the game! The entry point is the `main.py` file. If you used uv, you can run the following command:

```bash
uv run main.py
```

and the game will start.

Notice that the logic currently implemented is slightly different from the original one. 
In the real game, the third player can try to guess the word at any time, even interrupting the two players giving clues.
In this implementation, the third player (aka the LLM) can only guess the word after the two players have given their clues.
However, this might [change soon](https://platform.openai.com/docs/api-reference/streaming)...

## Disclaimer

This is just a fun project. I'm pretty sure it's not fun to play with an LLM. But whatever..
