from . import Prompt

class CheckWordValidityPrompt(Prompt):
    def __init__(self, word_or_phrase: str):
        self._word = word_or_phrase
        self._word_split = []
        for s in word_or_phrase.lower().split():
            tmp = ("".join([
                c for c in s
                if c in "abcdefghijklmnopqrstuvwxyz'0123456789"
            ]))
            if tmp:
                self._word_split.append(tmp)
        self._word_filtered = " ".join(self._word_split)

    def generate_system_prompt(self):
        return (
            "Your job is to determine whether a given word or phrase is ",
            "valid. A word or a phrase is valid if one of the following is "
            "true:\n"
            ""
            "- It can be found in a dictionary.\n"
            "- It is well-known and recognized by a certain group of people, "
            "and its meaning is known to others.\n"
            "\n"
            "Your answer must be a JSON object that contains two properties. "
            "First, a property whose key is 'is_valid' and its value is a "
            "JSON boolean 'true' if the word or phrase is valid, or 'false' "
            "otherwise. Second, a property whose key is 'is_offensive' and "
            "its value is a JSON boolean 'true' if the word of phrase is "
            "possibly offensive -- vulgar, obscene, sexual, racist, "
            "discriminatory, or contains strong language -- or 'false' "
            "otherwise.\n"
            "\n"
            "Your answer must be just a JSON object. Do not write anything "
            "else so that your answer is a valid, parsable JSON object."
        )

    def generate_prompt(self):
        if not self._word_split:
            return (
                "The user sent an invalid word. Just say {\"is_valid\": "
                "false, \"is_offensive\": false}, please."
            )
        return (
            "Determine whether the {word_or_phrase} \"{word_of_interest}\" "
            "is valid."
        ).format(
            word_or_phrase=('word' if len(self._word_split)==1 else 'phrase'),
            word_of_interest=self._word_filtered
        )
