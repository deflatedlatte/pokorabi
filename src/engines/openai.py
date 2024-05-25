from typing import List

from openai import OpenAI

import config
from . import Engine, Message

class OpenAIEngine(Engine):
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self._client = OpenAI(
            api_key=config.app_config.openai_api_key()
        )
        self._model = model

    def ask(self, prompt: Message, history: List[Message] = None):
        if history is not None:
            messages = [x.to_dict() for x in history]
        else:
            messages = []
        messages.append(prompt.to_dict())
        chat_completion = self._client.chat.completions.create(
            model=self._model,
            messages=messages
        )
        message = chat_completion.choices[0].message
        return Message(message.role, message.content)
