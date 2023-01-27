class Quiz_Brain:
    def __init__(self,questions):
        self.questions = questions
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_guess = input(f"Q{self.question_number}.) {current_question.text}: True or false: ")
        self.check_answer(current_question, user_guess)

    def still_has_questions(self):
        return self.question_number < len(self.questions)
            
    def check_answer(self, current_question,guess):
        if current_question.answer.lower() == guess.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"You got it incorrect, correct answer is {current_question.answer}")

        print(f"Your current score is {self.score}/{self.question_number}.")        
        print("\n")

          



        
        
