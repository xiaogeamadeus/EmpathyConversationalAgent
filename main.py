import argparse
import time

from agents.culturallyReviewer import CulturallyReviewer
from agents.simpleEnglishEditor import SimpleEnglishEditor
from controller import Controller
from managers.avoidingManager import AvoidingManager
from managers.empathyManager import Empathy
from managers.kaomojiManager import KaomojiManager
from agents.emotionRecognizer import EmotionRecognizer
from agents.compassionateListener import CompassionateListener

bot_name = "ListenerBot"


# def parse_args():
#     parser = argparse.ArgumentParser(description="Culturally Adaptive Conversational Agent")
#     return parser.parse_args()
#
#
# def generate_response(input_message):
#     if input_message == "exit":
#         return "Conversation ended."
#     # TODO: go to controller to solve else cases.


# args = parse_args()

class EmpathyConversationalAgent:
    def __init__(self):
        compassionate_listener = CompassionateListener()
        empathy_manager = Empathy()
        avoiding_manager = AvoidingManager()
        simple_english_editor = SimpleEnglishEditor()
        emotion_recognizer = EmotionRecognizer()
        culturally_reviewer = CulturallyReviewer()
        kaomoji_manager = KaomojiManager()
        self.controller = Controller(
            compassionate_listener=compassionate_listener,
            empathy_manager=empathy_manager,
            avoiding_manager=avoiding_manager,
            simple_english_editor=simple_english_editor,
            culturally_reviewer=culturally_reviewer,
            emotion_recognizer=emotion_recognizer,
            kaomoji_manager=kaomoji_manager
        )

    def converse(self, user_input):
        return self.controller.converse(user_input)



if __name__ == "__main__":
    conversation_active = False
    compassionate_listener = CompassionateListener()
    empathy_manager = Empathy()
    avoiding_manager = AvoidingManager()
    simple_english_editor = SimpleEnglishEditor()
    emotion_recognizer = EmotionRecognizer()
    culturally_reviewer = CulturallyReviewer()
    kaomoji_manager = KaomojiManager()
    controller = Controller(
        compassionate_listener=compassionate_listener,
        empathy_manager=empathy_manager,
        avoiding_manager=avoiding_manager,
        simple_english_editor=simple_english_editor,
        culturally_reviewer=culturally_reviewer,
        emotion_recognizer=emotion_recognizer,
        kaomoji_manager=kaomoji_manager
    )
    # TODO: Compile the previous messages
    print(bot_name + ": Thank you so much for your time and courage to talk with me. I am really sorry that it was the "
                     "situation that brought you here today.\n But it takes great strength to walk through those doors "
                     "and say: 'I need help'.")
    time.sleep(5)
    print(bot_name + ": Before we start talking, please confirm that you are safe now and let yourself keep in a "
                     "relaxed environment.")
    time.sleep(3)

    print(bot_name + ": Are you in a safe environment without anyone else who will give you pressure? Please "
                     "type 'yes' or 'no'")

    # Safety environment check
    safe_check = False
    is_safe = True
    while not safe_check:
        user_input = input("User: ")
        if user_input == "yes":
            print(bot_name + ": I'm really happy to hear that you are safe now!")
            safe_check = True
        elif user_input == "no":
            print(
                bot_name + ": Please close this website, delete the browser record in your phone or computer and take "
                           "care, hoping to talk with you in next time!")
            safe_check = True
            is_safe = False
        else:
            print(bot_name + "It looks like that you type a wrong options, could you please type 'yes' or 'no' in here?")

    if is_safe:
        time.sleep(1)
        print(bot_name + ": I'm " + bot_name + ", a robot created by Kyoto University's researchers. My job is to "
                                               "talk to people who are stressed and try to enlighten them.")
        time.sleep(5)
        print(bot_name + ": Please feel free to talk anything to me. All the record of conversation will be deleted in "
                         "your phone or computer.\n Nobody will know what we have talked before after closing this "
                         "website.")
        time.sleep(5)
        print(bot_name + ": By the way, please confirm that would you mind letting researchers from Kyoto University"
                         "use our conversation data to make me more smart and can talk more things to you.\n"
                         "Feel free to do the decision cause if you say 'No', you can also talk with me as well. We "
                         "respect your choices.")
        time.sleep(5)
        print(bot_name + ": Would you mind if the researchers use this conversation data? (This conversation only) "
                         "Please type 'yes' or 'no'")

        # Confidential check process
        confidential_check = False
        while not confidential_check:
            user_input = input("User: ")
            if user_input == "yes":
                print(bot_name + ": Thank you so much for sharing data to us! Researchers will try them best to make me"
                                 " more smart and easy to talk with!")
                confidential_check = True
            elif user_input == "no":
                print(
                    bot_name + ": The data will not be shown to the researchers, it will be a secret between you and "
                               "me:D")
                confidential_check = True
            else:
                print(bot_name + "It looks like that you type a wrong options, could you please type 'yes' or 'no' in "
                                 "here?")
        time.sleep(1)
        print(bot_name + ": Are you ready for talking with me? Please type 'start' to have a free chat!")
        # Real conversation
        while True:
            user_input = input("User: ")
            if user_input == "exit":
                break  # User input "exit" to end the conversation
            if user_input == "start":
                conversation_active = True
                print(bot_name + ": Conversation started. Please talk anything you hope to share so far! By the way, "
                                 "you can type 'exit' to close our conversation in anytime you want!")
            elif conversation_active:
                agent_response = controller.converse(user_input)
                print(bot_name + ": ", agent_response)
            else:
                print(bot_name + ": It looks like that you type a wrong options, could you please type 'start' to "
                                 "start the conversation?")
        # TODO: Add the end messages
        print(bot_name + ": Thank you very much for talking with me! Please don't forget to close this website, "
                         "delete your browser record in your phone and computer. "
                         "If you hope to talk with me again, please keep our website in a safe place~ "
                         "Looking forward to talking with you again! Have a nice day:D")
