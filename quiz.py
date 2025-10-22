# Trivia Quiz Game

questions = [
    {
        "question": "What is the capital of Japan?",
        "options": ["Seoul", "Tokyo", "Beijing", "Bangkok"],
        "answer": 1
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Gold", "Oxygen", "Osmium", "Opal"],
        "answer": 1
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Oscar Wilde", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": 1
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Saturn", "Jupiter", "Mars"],
        "answer": 2
    },
    {
        "question": "Which year did the Titanic sink?",
        "options": ["1905", "1912", "1920", "1898"],
        "answer": 1
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Iron", "Diamond", "Quartz", "Granite"],
        "answer": 1
    },
    {
        "question": "Which country is home to the kangaroo?",
        "options": ["South Africa", "India", "Australia", "Brazil"],
        "answer": 2
    },
    {
        "question": "How many continents are there?",
        "options": ["5", "6", "7", "8"],
        "answer": 2
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["90°C", "100°C", "120°C", "80°C"],
        "answer": 1
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"],
        "answer": 1
    }
]

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for idx, option in enumerate(q['options']):
            print(f"{idx + 1}. {option}")
        try:
            user_answer = int(input("Your answer (1-4): ")) - 1
            if user_answer == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['options'][q['answer']]}")
        except ValueError:
            print("⚠️ Invalid input. Skipping question.")

    print(f"\n🎓 Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 Perfect score! You're a trivia master!")
    elif score >= len(questions) // 2:
        print("👍 Great job!")
    else:
        print("📚 Keep practicing!")

if __name__ == "__main__":
    while True:
        run_quiz(questions)
        again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thanks for playing! See you next time.")
            break
