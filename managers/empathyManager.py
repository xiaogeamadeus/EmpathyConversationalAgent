from agents.emotionRecognizer import Emotion
from collections import deque

from agents.empathyAgents.lowLevelEmpathyAgent import LowLevelEmpathyAgent
from agents.empathyAgents.midLevelEmpathyAgent import MidLevelEmpathyAgent
from agents.empathyAgents.highLevelEmpathyAgent import HighLevelEmpathyAgent


class Empathy:
    def __init__(self):
        self.emotion_queue = deque()
        self.emotion_queue.append(Emotion('joy', 30))
        self._low_level_agent = LowLevelEmpathyAgent()
        self._mid_level_agent = MidLevelEmpathyAgent()
        self._high_level_agent = HighLevelEmpathyAgent()

    def get_low_level_response(self, user_input):
        # Contact with low-level agent
        return self._low_level_agent.run_agent(user_input)

    def get_mid_level_response(self, user_input, listener_response):
        return self._mid_level_agent.run_agent(user_input, listener_response)

    def get_high_level_response(self, user_input, listener_response):
        return self._high_level_agent.run_agent(user_input, listener_response)

    # def emotion_regulation(self, emotion_data):
    #     if emotion_data:
    #         max_value = 0
    #         max_emotion = ""
    #         for emotion in emotion_data:
    #             if emotion is not None:
    #                 if max_value < emotion['value']:
    #                     max_emotion = emotion['emotion']
    #                     max_value = emotion['value']
    #
    #     goal = self.find_goals(max_emotion)
    #
    #     return max_emotion, goal
    #
    # def find_goals(self, cur_emotion):
    #     goal = ""
    #     if cur_emotion != "":
    #         if cur_emotion == "sadness":
    #             goal = "make him happy."
    #         elif cur_emotion == "fear":
    #             goal = "Tell him not to be afraid."
    #         elif cur_emotion == "joy":
    #             goal = "Tell him not to be blindly optimistic."
    #         elif cur_emotion == "anger":
    #             goal = "make him calm down."
    #         elif cur_emotion == "surprise":
    #             goal = "let him try to remember who helped him."
    #     return goal
