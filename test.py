from agents.emotionRecognizer import EmotionRecognizer
from managers.avoidingManager import AvoidingManager
from agents.empathyAgents.lowLevelEmpathyAgent import LowLevelEmpathyAgent

# avoiding = AvoidingManager()
emotion_recogn = EmotionRecognizer()
low_level = LowLevelEmpathyAgent()
#
test1 = "Could you please tell me why you do not say something?"
test2 = "A great thing is that my women friend can talk with me and help me reduce some stress. But we cannot see and chat with each other usually."
# test2 = "Could you please tell me why you do not try to do something and say?"
# print(emotion_recogn.run_agent(test1))
# print(emotion_recogn.run_agent(test2))

res = emotion_recogn.run_agent(test2)
print(res.emotion)
print(res.rate)
#
# print("res1: " + str(avoiding.checkDuplicate(test1)))
# print("res2: " + str(avoiding.checkDuplicate(test2)))


