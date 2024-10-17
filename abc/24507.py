questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere? ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")
options = (("A. ","B. ","C. ","D."),
("A. ","B. ","C. ","D."),
("A. ","B. ","C. ","D."),
("A. ","B. ","C. ","D."),
("A. ","B. ","C. ","D."))
answers = ("C","D","A","B","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Make a guess: ")
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    question_num += 1
print(f"YOUR SCORE : {score}")