questions = [
    {
        "q": "What is the capital of France?",
        "options": ["A) Berlin", "B) Paris", "C) Madrid", "D) Rome"],
        "answer": "B"
    },
    {
        "q": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
        "answer": "C"
    },
    {
        "q": "Who wrote 'Hamlet'?",
        "options": ["A) Dickens", "B) Shakespeare", "C) Orwell", "D) Twain"],
        "answer": "B"
    }
]

score = sum(
    input(f"\nQ{i+1}: {q['q']}\n" + "\n".join(q['options']) + "\n Choose Option(A,B,C,D): ").strip().upper() == q["answer"]
    for i, q in enumerate(questions)
)
print(f"\nYou got {score}/{len(questions)} correct!")