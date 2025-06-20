def display_question(question_text, answers, question_type="multiple_choice"):
    print(f"\nQuestion: {question_text}")
    
    if question_type in ["multiple_choice", "true_false"]:
        if answers:
            for i, answer in enumerate(answers, 1):
                print(f"{i}. {answer}")
        else:
            print("Options not available.")
    elif question_type == "open_ended":
        print("Type your answer:")
    else:
        print("Unknown question type.")


def check_answer(user_answer, correct_answer, question_type):
    if question_type in ["multiple_choice", "true_false"]:
        return user_answer.strip() == correct_answer
    else:
        return user_answer.strip().lower() == correct_answer.lower()

def show_feedback(is_correct, question_type, correct_answer=None):
    if is_correct:
        print("✅ Correct! Shabbash!")
    else:
        print("❌ Wrong hai chutiyee bkl.")
        if question_type != "open_ended":
            print(f"The correct answer was: {correct_answer}")

def initialize_game():
    score = 0
    current_question = 0
    rounds = 1
    return score, current_question, rounds

def start_game(questions, score, current_question, rounds):
    while True:
        print(f"\n🔄 Round {rounds} | Current Score: {score}\n")
        q = questions[current_question]
        q_text = q['text']
        answers = q['answers']
        correct = q['correct']
        q_type = q['type']

        display_question(q_text, answers, q_type)

        user_answer = input("Your answer (or 'quit' to exit): ").strip()
        if user_answer.lower() == "quit":
            break

        is_correct = check_answer(user_answer, correct, q_type)
        if is_correct:
            score += 10

        show_feedback(is_correct, q_type, correct)
        print(f"Explanation: {q.get('explanation', 'No explanation provided.')}")
        
        current_question = (current_question + 1) % len(questions)
        play_again = input("\nDo you want another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break
        rounds += 1

def game_over(score):
    print("\n🎉 Game Over!")
    print(f"🏆 Your final Score: {score}")
    print("Thanks for Playing!")
