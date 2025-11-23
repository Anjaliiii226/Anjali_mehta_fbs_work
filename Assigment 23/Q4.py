# Quiz data: Question, Options, Correct Answer
quiz = [
    {
        "question": "1. What is the capital of India?",
        "options": {"A": "Mumbai", "B": "Delhi", "C": "Kolkata", "D": "Chennai"},
        "answer": "B"
    },
    {
        "question": "2. Which is the largest planet in the Solar System?",
        "options": {"A": "Mars", "B": "Earth", "C": "Jupiter", "D": "Saturn"},
        "answer": "C"
    },
    {
        "question": "3. What does CPU stand for?",
        "options": {"A": "Central Process Unit", "B": "Central Processing Unit",
                    "C": "Control Processing Unit", "D": "Central Program Unit"},
        "answer": "B"
    }
]

score = 0

print("----- QUIZ GAME -----\n")

for q in quiz:
    print(q["question"])
    for key, value in q["options"].items():
        print(f"   {key}. {value}")

    user_ans = input("Enter your answer (A/B/C/D): ").upper()

    if user_ans == q["answer"]:
        print("✔ Correct!\n")
        score += 1
    else:
        print(f"✘ Incorrect! Correct Answer is: {q['answer']}\n")

print("----- QUIZ FINISHED -----")
print(f"Your Score: {score} / {len(quiz)}")
