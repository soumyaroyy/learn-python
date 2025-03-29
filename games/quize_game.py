# import json

def load_questions():
    return [
        {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": "C"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"], "answer": "B"},
        {"question": "What is the largest ocean on Earth?", "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"], "answer": "D"},
        {"question": "Who wrote 'Hamlet'?", "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"], "answer": "B"}
    ]

def run_quiz():
    questions = load_questions()
    score = 0
    
    print("Welcome to the Quiz Game!\n")
    
    for index, q in enumerate(questions, start=1):
        print(f"{index}. {q['question']}")
        for option in q["options"]:
            print(option)
        
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    
    print(f"Quiz over! Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
