from agents.compassionateListener import CompassionateListener

bot_name = "ListenerBot"

listener = CompassionateListener()
conversation_active = False

while True:
    user_input = input("User: ")
    if user_input == "exit":
        break  # User input "exit" to end the conversation
    if user_input == "start":
        conversation_active = True
        print(bot_name + ": Conversation started. Please talk anything you hope to share so far! By the way, "
                         "you can type 'exit' to close our conversation in anytime you want!")
    elif conversation_active:
        agent_response = listener.run_agent(user_input)
        print(bot_name + ": ", agent_response)
    else:
        print(bot_name + ": It looks like that you type a wrong options, could you please type 'start' to "
                         "start the conversation?")