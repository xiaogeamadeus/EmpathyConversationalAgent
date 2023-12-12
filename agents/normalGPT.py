import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("openai_api_key")


class NormalGPT:
    def __init__(self):
        self.client = OpenAI(api_key=api_key)

    def run_agent(self, user_input):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
        )

        return response.choices[0].message.content
