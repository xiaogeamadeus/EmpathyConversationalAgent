import time
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("openai_api_key")


class MidLevelEmpathyAgent:

    def __init__(self):
        self.client = OpenAI(api_key=api_key)

    def wait_for_run_completion(self, thread_id, run_id):
        while True:
            time.sleep(1)
            run = self.client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            print(f"MidLevelEmpathyAgent, Current run status: {run.status}")
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

    def run_agent(self, user_input, listener_response):
        assistant = self.client.beta.assistants.create(
            name="Mid-level Empathy Editor",
            description="Motor Mimicry & Emotional Contagion",
            instructions="You are an Empathy Editor. The task of you is doing emotional contagion of the "
                         "input sentences. you will accept two sentences, the first sentence is user's response, "
                         "the second one is a possible response. Your task is editing the possible response. First, "
                         "you should start with an emotional carryover, assuming that you are that user and that "
                         "tweaking the response will give the other person heartfelt comfort. The input will like "
                         "user:'', response: ''.",
            model="gpt-4-1106-preview"
        )

        assistant_id = assistant.id
        # print(f"Assistant ID: {assistant_id}")

        thread = self.client.beta.threads.create()
        # print(f"Thread: {thread}")

        # Create a message
        new_input = "user: " + user_input + ", response: " + listener_response
        message = self.client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=new_input,
        )

        # Create a run
        run = self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id,
        )

        # Wait for run to complete
        run = self.wait_for_run_completion(thread.id, run.id)

        if run.status != 'completed':
            print("mid-level: ",run.error)
        else:
            # Return the latest messages from the thread
            messages = self.client.beta.threads.messages.list(thread_id=thread.id)
            for msg in messages:
                return f"{msg.content[0].text.value}"






