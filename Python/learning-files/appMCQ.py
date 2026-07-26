from QuestionClass import Question

question_prompts = [
    "What is the capital of France?\n(a) Berlin\n(b) Madrid\n(c) Paris\n\n",
    "What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n\n",
    "What is the largest ocean on Earth?\n(a) Atlantic Ocean\n(b) Indian Ocean\n(c) Pacific Ocean\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]

score = 0

for question in questions:
    answer = input(question.question)
    if answer.lower() == question.answer:
        score += 1
    else:
        pass

print(f"You got {score}/{len(questions)} correct.") 