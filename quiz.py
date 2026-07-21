quiz = [
    {
        "question": "What is the capital of India?",
        "option" : ["Mumbai","Delhi","Kolkata","Chennai"],
        "answer" : "Delhi"      
    },
    {
        "question" : "Which language is used in AI?",
        "option" : ["Python","Java","CSS","HTML"],
        "answer" : "Python"
    },
    {
        "question" : "what is my name?",
        "option" : ["Abinaya","abina","abin","abiya"],
        "answer" : "Abinaya"
    },
]

score = 0
for i, q in enumerate(quiz, start=1):
    print(f"\nQuestion {i} : {q['question']}")
    for j, option in enumerate(q["option"], start=1):
        print(f"{j}. {option}")

        choice = int(input("Enter your choice (1-4): "))
        selected = q["option"][choice - 1]

    if selected == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}")

print("\nQuiz Completed!")
print(f"Your final score is:, {score}/{len(quiz)}")
print(f"Your percentage is:, {score / len(quiz) * 100}%")