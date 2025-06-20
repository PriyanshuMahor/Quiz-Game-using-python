""" QUIZ GAME PROJECT """
from display import display_welcome
from computing_functions import initialize_game, start_game, game_over
from questions import multiple_choice_questions, load_questions

# Cleaned-up and standardized question format

def main():
    display_welcome()
    questions = load_questions('questions.json')
    score, current_question, rounds = initialize_game()
    start_game(questions, score, current_question, rounds)
    game_over(score)

if __name__ == "__main__":
    main()
