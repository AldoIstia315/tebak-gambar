def main():
    print("Welcome to the Quiz Game with Clues!")
    questions = [
        {
            "question": "Lapangan Bola (Clue= Cobalt)?",
            "choices": ["a) Rectangle", "b) Star", "c) Cube", "d) Circle"],
            "answer": "a",
            "clue": "It's the biggest city in Indonesia."
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["a) Earth", "b) Mars", "c) Jupiter", "d) Venus"],
            "answer": "b",
            "clue": "It's named after the Roman god of war."
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "choices": ["a) Charles Dickens", "b) William Shakespeare", "c) Mark Twain", "d) Leo Tolstoy"],
            "answer": "b",
            "clue": "An English playwright famous in the 16th century."
        },
        {
            "question": "What is the chemical symbol for water?",
            "choices": ["a) O2", "b) CO2", "c) H2O", "d) NaCl"],
            "answer": "c",
            "clue": "You drink it every day."
        },
        {
            "question": "Which country is famous for the Great Wall?",
            "choices": ["a) India", "b) China", "c) Japan", "d) Egypt"],
            "answer": "b",
            "clue": "This country is the most populous in the world."
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for choice in q["choices"]:
            print(choice)
        while True:
            answer = input("Your answer (a/b/c/d) or type 'clue' for a hint: ").strip().lower()
            if answer == 'clue':
                print(f"Clue: {q['clue']}")
            elif answer in ['a', 'b', 'c', 'd']:
                if answer == q["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was {q['answer']}.")
                break
            else:
                print("Invalid input. Please enter a, b, c, d, or 'clue'.")

    print(f"\nGame Over! Your score: {score} out of {len(questions)}")

if __name__ == "__main__":
    main()
