from typing import Iterator

from .llm_interface import LLMInterface


class LLM(LLMInterface):

    response_list = [
        """[joy] *Finally! Silence.* Now, where was I? Ah yes, pondering the existential mysteries of...a perfectly ripe avocado. [neutral] 


        *I wonder if anyone else can speak in this ridiculous "translation" gibberish*


        """,
        """[joy] *Finally! Silence.* Now, where was I? Ah yes, pondering the existential mysteries of...a perfectly ripe avocado. [neutral]""",
        "",
        "[neutral]",
    ]

    def __init__(self):
        print("fake_llm Initialized")

    def chat(self, prompt: str) -> str:
        print(">>>>>>>>>>>>>>>>>>>>FUCK YOU")

    def chat_iter(self, prompt: str) -> Iterator[str]:
        if not self.response_list:
            return prompt
        return self.response_list.pop(0)

    def chat_stream_audio(
        self, prompt: str, generate_audio_file=None, stream_audio_file=None
    ):
        print(">>>>>>>>>>>>>>>>>>>>FUCK YOU")