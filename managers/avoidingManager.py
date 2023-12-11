from agents.duplicateCheckerAgents.duplicateChecker import DuplicateChecker
from agents.duplicateCheckerAgents.isQuestionChecker import IsQuestionChecker
from agents.duplicateCheckerAgents.questionExtractor import QuestionExtractor


class AvoidingManager:
    def __init__(self):
        self.question_list = []
        self.duplicateChecker = DuplicateChecker()
        self.question_extractor = QuestionExtractor()
        self.is_question_checker = IsQuestionChecker()

    def checkDuplicate(self, listener_response):

        is_question = self.is_question_checker.run_agent(listener_response)
        print("is question result: " + str(is_question))
        if is_question == "False":
            return False
        elif is_question != "True":
            print("INFO: Is question checker have some error response.")

        flag = False
        extracted_question = self.question_extractor.run_agent(listener_response)
        print("extracted_question: " + extracted_question)
        for question in self.question_list:
            check_message = "Sentence1: " + extracted_question + ". Sentence2: " + question
            compare_res = self.duplicateChecker.run_agent(check_message)
            print("compare res: " + compare_res)
            if compare_res == "True":
                flag = True
                break
            elif compare_res == "False":
                continue
            else:
                print("INFO: Duplicate Checker have some error response.")
        self.question_list.append(extracted_question)
        return flag
