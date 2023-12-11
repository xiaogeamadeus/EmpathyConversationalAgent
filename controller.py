import logging
from agents.emotionRecognizer import Emotion

logger = logging.getLogger().getChild(__name__)


class Controller:
    def __init__(self, compassionate_listener, empathy_manager, avoiding_manager, simple_english_editor,
                 culturally_reviewer, emotion_recognizer, kaomoji_manager):
        self._compassionate_listener = compassionate_listener
        self._empathy_manager = empathy_manager
        self._avoiding_manager = avoiding_manager
        self._simple_english_editor = simple_english_editor
        self._culturally_reviewer = culturally_reviewer
        self._emotion_recognizer = emotion_recognizer
        self._kaomoji_manager = kaomoji_manager
        self.rate_sum = 30
        self.prev_level = "NULL"  # "NULL", "LOW", "MID"
        # self.emotions_queue = []

    def get_emotion(self, user_input) -> Emotion:
        return self._emotion_recognizer.run_agent(user_input)

    def diff_of_new_emotion_from_average_ten(self, new_emotion):
        # Check the diff of new emotion rate and average of latest 10 emotion rate bigger than 30 or not
        flag = False
        emotion_q = self._empathy_manager.emotion_queue
        sz = len(emotion_q)

        if new_emotion.rate - self.rate_sum // sz >= 30 or new_emotion.rate >= 80:
            flag = True
        if sz >= 10:
            removed_e = emotion_q.popleft()
            self.rate_sum -= removed_e.rate
        self.rate_sum += new_emotion.rate

        emotion_q.append(new_emotion)

        return flag

    def get_listener_message(self, user_input, origin_messages=""):
        # if origin message not empty, will generate response with a different question
        return self._compassionate_listener.run_agent(user_input, old_messages=origin_messages)

    # def emotion_become_negative(self, cur_emotion):
    #     negative_emotions = {"sad", "anger", "fear", "disgust"}
    #     positive_emotions = {"joy", "surprise", "disgust"}
    #     emotion_list = self._empathy_manager.emotion_queue
    #     if not emotion_list:
    #         # Use empathy mechanism when start with negative emotions
    #         return cur_emotion in negative_emotions
    #     pre = emotion_list[-1]
    #     if cur_emotion in negative_emotions and pre in positive_emotions:
    #         # emotion have changed from negative to positive
    #         return True
    #     return False

    def converse(self, user_input):

        # Empathy manager
        # Class Emotion: emotion, rate
        cur_emotion = self.get_emotion(user_input)

        # Detect emotion rate diff:
        if self.prev_level == "NULL" and self.diff_of_new_emotion_from_average_ten(cur_emotion):
            # new emotion had diff and no emotions so far
            self.prev_level = "LOW"
            # only record it in listener thread.
            origin_response = self.get_listener_message(user_input)
            empathy_response = self._empathy_manager.get_low_level_response(user_input)
            return self._kaomoji_manager.generate_kaomoji(cur_emotion, empathy_response)

        elif self.prev_level == "LOW":
            origin_response = self.get_listener_message(user_input)
            empathy_response = self._empathy_manager.get_mid_level_response(user_input, origin_response)

            self.prev_level = "MID"
        elif self.prev_level == "MID":
            origin_response = self.get_listener_message(user_input)
            empathy_response = self._empathy_manager.get_high_level_response(user_input, origin_response)
            self.prev_level = "NULL"
        else:
            # Normal cases
            origin_response = self.get_listener_message(user_input)
            # Duplicate question check
            # while self._avoiding_manager.checkDuplicate(origin_response):
            #     origin_response = self.get_listener_message(user_input, origin_messages=origin_response)
            empathy_response = origin_response
        # if self.emotion_become_negative(cur_emotion):
        #     # emotion became negative from prev_emotion or start from negative
        #     empathy_response = self._empathy_manager.start_three_level_empathy(origin_response)
        # else:
        #     empathy_response = origin_response
        # self._empathy_manager.emotion_queue.append(cur_emotion)

        # Culturally reviewer
        # if self._culturally_reviewer.culturally_check(empathy_response) == "false":
        # Simple English Editor
        simple_response = self._simple_english_editor.run_agent(empathy_response)
        return simple_response
