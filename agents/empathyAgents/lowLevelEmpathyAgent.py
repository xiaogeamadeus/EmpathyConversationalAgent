import time
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("openai_api_key")


class LowLevelEmpathyAgent:

    def __init__(self):
        self.client = OpenAI(api_key=api_key)

    def wait_for_run_completion(self, thread_id, run_id):
        while True:
            time.sleep(1)
            run = self.client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            print(f"LowLevelEmpathyAgent, Current run status: {run.status}")
            if run.status in ['completed', 'failed', 'requires_action']:
                return run

    # def print_messages_from_thread(self, thread_id):
    #     messages = self.client.beta.threads.messages.list(thread_id=thread_id)
    #     messages_local = []
    #     for msg in messages:
    #         messages_local.append(f"{msg.role}: {msg.content[0].text.value}")
    #     messages_local.reverse()
    #     for msg in messages_local:
    #         print(msg)

    # def print_latest_message(self, thread_id):
    #     messages = self.client.beta.threads.messages.list(thread_id=thread_id)
    #     for msg in messages:
    #         print(f"{msg.role}: {msg.content[0].text.value}")
    #         break

    def run_agent(self, user_input):
        assistant = self.client.beta.assistants.create(
            name="Low-level Empathy Editor",
            description="Mimicry & Emotional Carryover",
            instructions="You are a chatbot with empathy. I will give you sentences with strong emotions, please give "
                         "a quick and really short response, which just let user know you are current listening "
                         "kindly and felt the same emotion. For example: 'I see... it's terrible'. Please do not ask "
                         "any question. Every input will be independent.",
            model="gpt-4-1106-preview"
        )

        assistant_id = assistant.id
        # print(f"Assistant ID: {assistant_id}")

        thread = self.client.beta.threads.create()
        # print(f"Thread: {thread}")

        # Create a message
        message = self.client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )

        # Create a run
        run = self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id,
        )

        # Wait for run to complete
        run = self.wait_for_run_completion(thread.id, run.id)

        if run.status != 'completed':
            print("low-level error")
        else:
            # Return the latest messages from the thread
            messages = self.client.beta.threads.messages.list(thread_id=thread.id)
            for msg in messages:
                return f"{msg.content[0].text.value}"






