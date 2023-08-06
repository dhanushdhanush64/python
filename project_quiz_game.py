class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# List of questions and answers
questions = [
    Question("What is the capital of France?", "Paris"),
    Question("What is 2 + 2?", "4"),
    Question("Which planet is known as the Red Planet?", "Mars")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt + " ")
        if user_answer.lower() == question.answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question.answer, "\n")
    
    print("Quiz completed. Your score:", score, "out of", len(questions))

if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    run_quiz(questions)
