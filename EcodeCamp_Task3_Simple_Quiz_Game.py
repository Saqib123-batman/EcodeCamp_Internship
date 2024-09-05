questions = ("Which ocean is called 'Herring pond'?: ",
                       "Copper is used in the production of?: ",
                       "Elements extracted from sea water?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")

options = (("A. Pacific Ocean ", "B. Arctic Ocean", "C. Atlantic Ocean", "D. Indian OCean"),
                   ("A. Brick klins", "B. Children toys", "C. Kitchen utilities", "D. Electric wires"),
                   ("A. Nitrogen", "B. Magnesium", "C. Carbon", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "B", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")