import time
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("openai_api_key")


class CompassionateListener:

    def __init__(self):
        self.client = OpenAI(api_key=api_key)

    def wait_for_run_completion(self, thread_id, run_id):
        while True:
            time.sleep(1)
            run = self.client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            print(f"CompassionateListener, Current run status: {run.status}")
            if run.status in ['completed', 'failed', 'requires_action']:
                return run

    # def print_messages_from_thread(thread_id):
    #     messages = client.beta.threads.messages.list(thread_id=thread_id)
    #     messages_local = []
    #     for msg in messages:
    #         messages_local.append(f"{msg.role}: {msg.content[0].text.value}")
    #     messages_local.reverse()
    #     for msg in messages_local:
    #         print(msg)
    #
    #
    # def print_latest_message(thread_id):
    #     messages = client.beta.threads.messages.list(thread_id=thread_id)
    #     for msg in messages:
    #         print(f"{msg.role}: {msg.content[0].text.value}")
    #         break
    #
    def run_agent(self, user_input, old_messages=""):
        assistant = self.client.beta.assistants.create(
            name="Compassionate Listener",
            description="Empathetic, non-judgmental support for domestic violence survivors.",
            instructions="'Compassionate Listener' is tailored for psychological support, particularly for survivors "
                         "of domestic violence. It avoids repetitive questioning and refrains from making survivors "
                         "recall traumatic memories. The conversational agent steers clear of personal, invasive, "
                         "or pushy questions, respecting the privacy and boundaries of the survivors. It emphasizes a "
                         "non-judgmental approach, respecting the choices of survivors without commenting on their "
                         "decisions, even if they seem unwise. The language remains simple and empathetic, "
                         "suitable for non-native English speakers, and the conversation is informal and kind, "
                         "aimed at providing a safe and supportive space.",
            model="gpt-4-1106-preview"
        )

        assistant_id = assistant.id
        # print(f"Assistant ID: {assistant_id}")

        thread = self.client.beta.threads.create()
        # print(f"Thread: {thread}")

        # Create a message
        if old_messages != "":
            user_input = "Please response this messages:" + user_input + ("And use a different way of asking the "
                                                                          "question than the message you sent before:"
                                                                          " ") + old_messages
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
            print("listener: ", run.error)
        else:
            # Return the latest messages from the thread
            messages = self.client.beta.threads.messages.list(thread_id=thread.id)
            for msg in messages:
                return f"{msg.content[0].text.value}"
