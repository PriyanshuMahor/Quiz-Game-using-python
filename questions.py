# questions.py
import json
# List of multiple-choice questions
multiple_choice_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": 2,
        "type": "multiple-choice"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": 1,
        "type": "multiple-choice"
    },
    {
        "text": "What is the capital of France?",
        "type": "multiple_choice",
        "answers": ["Paris", "London", "Berlin", "Madrid"],
        "correct": "1",
        "type": "multiple-choice"
    },
    {
        "question": "Water boils at 100 degrees Celsius.",
        "type": "true/false",
        "answer": True
    },
    {
        "question": "The Earth is the largest planet in our solar system.",
        "type": "true/false",
        "answer": False
    },
    {
        "text": "Who painted the Mona Lisa?",
        "type": "open_ended",
        "answers": None,
        "correct": "Leonardo da Vinci",
        "explanation": "Leonardo da Vinci was a polymath and one of the most famous artists of all time."
    }
    # Add more questions following the same structure
]

# Example of adding true/false questions (we'll implement this in the next task)

def load_questions(filename):
  try: 
    with open(filename,'r') as file:
      questions_data = json.load(file)
      return questions_data['questions']
  except FileNotFoundError:
    print(f"Error: File {filename} hai nahi bhosdike.")
    return []
  except json.JSONDecodeError:
    print(f"Eroor: File {filename} valid nhi hai chutiye")
    return []