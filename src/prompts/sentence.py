from . import Prompt

class RequestSentencesPrompt(Prompt):
    def __init__(self, word: str, number_of_sentences: int = 10):
        self._word = word
        self._number_of_sentences = number_of_sentences

    def generate_prompt(self):
        return (
            "Give me {number_of_sentences} example sentences that use the "
            "word '{word}'. For each example, please surround the word with "
            "double square brackets, like [[word]], so that I can easily see "
            "where the word I requested is. Your answer must be a JSON list "
            "that contains the example sentences as JSON strings, like the "
            "following:\n"
            "\n"
            "[\n"
            "    \"...\",\n"
            "    \"...\",\n"
            "    \"...\"\n"
            "]\n"
            "\n"
            "Please say no more than the JSON list as requested above, so "
            "that I can parse what you give."
        ).format(
            number_of_sentences=self._number_of_sentences,
            word=self._word
        )
