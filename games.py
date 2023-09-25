import time
questions = {
    "What are two things you can never eat for breakfast?": "Lunch and Dinner",
    "What is always coming but never arrives?": "Tomorrow",
    "What can be broken but never held?": "Promise",
    "2**8 = " : "256",
    "Do you like the question? " : "Yes"
}

score = 0


def user_answer(self):
    user_answer = input("Please enter your answer: ")
    return user_answer.lower()

def ask_question(question, correct_answer):
    global score  
    print(question)
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect, the correct answer is {correct_answer}\n")

def run_quiz():
    print("Welcome to the Quiz Game :)")
    time.sleep(1)
    print("You will have 30 seconds to answer each question.")
    time.sleep(1)
    print("Let's get started!")
    time.sleep(1)

    for question, answer in questions.items():
        print("Time remaining: 30 seconds")
        time_limit = 30

        start_time = time.time()
        ask_question(question, answer)
        end_time = time.time()

        time_taken = end_time - start_time
        time_remaining  = time_limit - time_taken

        if time_remaining <= 0:
            print("Time's up!\n")
            break
            
        else:
            print(f"Time remaining: {int(time_remaining)} seconds\n")
            time.sleep(1)

    print(f"Quiz completed! Final score is: {score}/{len(questions)}")

run_quiz()
