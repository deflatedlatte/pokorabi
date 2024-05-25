import json

from fastapi import APIRouter

import config
from engines import Message
from engines.openai import OpenAIEngine
from prompts.sentence import RequestSentencesPrompt
from prompts.word import CheckWordValidityPrompt

router = APIRouter()

@router.get("/sentences")
def get_sentences(word: str):
    engine = OpenAIEngine()
    prompt = RequestSentencesPrompt(word)
    user_message = Message("user", prompt.generate_prompt())
    assistant_message = engine.ask(user_message)
    return json.loads(assistant_message.content)

@router.get("/words/validity")
def get_word_validity(word: str):
    engine = OpenAIEngine()
    prompt = CheckWordValidityPrompt(word)
    system_prompt = Message("system", prompt.generate_system_prompt())
    user_message = Message("user", prompt.generate_prompt())
    assistant_message = engine.ask(user_message, [system_prompt])
    return json.loads(assistant_message.content)

