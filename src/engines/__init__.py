from typing import List

class Message:
    def __init__(self, role: str, content: str):
        self._role = role
        self._content = content

    @property
    def role(self):
        return self._role

    @property
    def content(self):
        return self._content

    def to_dict(self):
        return {
            "role": self._role,
            "content": self._content
        }

class Engine:
    def ask(self, prompt: Message, history: List[Message]):
        return Message("assistant", "")
