from agents.emotionRecognizer import EmotionRecognizer
from managers.avoidingManager import AvoidingManager
from agents.empathyAgents.lowLevelEmpathyAgent import LowLevelEmpathyAgent

# avoiding = AvoidingManager()
emotion_recogn = EmotionRecognizer()
low_level = LowLevelEmpathyAgent()
#
test1 = "Could you please tell me why you do not say something?"
test2 = "He'd come and beat me up at work no matter what kind of shit was going on. Everytime when I do something not satisfied him, he will beat me, The scariest thing is that my kids are turning into men like him."
# test2 = "Could you please tell me why you do not try to do something and say?"
# print(emotion_recogn.run_agent(test1))
# print(emotion_recogn.run_agent(test2))

print(emotion_recogn.run_agent(test2))
#
# print("res1: " + str(avoiding.checkDuplicate(test1)))
# print("res2: " + str(avoiding.checkDuplicate(test2)))


