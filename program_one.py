# -*- coding: utf-8 -*-
"""program_one.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KIDGd1DVgjl9S2gI6vRmtGaIJo7o54HE
"""

import os
from exam import Exam
from setup import extract_questions

def parse_cmd_args():
    try:
        directory = input("Enter the directory path: ").strip()
        duration = int(input("Enter the exam duration (in minutes): ").strip())
        shuffle = input("Enter shuffle mode (Y/N): ").strip().lower()
        question_file = input("Enter the name of the questions file: ").strip()
    except ValueError:
        print("Duration must be an integer.")
        return None

    # Check if shuffle is 'Y' or 'N' and convert to a boolean
    shuffle = shuffle == 'Y'

    return directory, duration, shuffle, question_file

def setup_exam():
    setup_choice = parse_cmd_args()

    if setup_choice:
        directory, duration, shuffle, question_file = setup_choice
    else:
        return None, False

    try:
        # Combine the directory and file name to get the full path
        questions_file = os.path.join(directory, question_file)

        with open(questions_file, "r") as file:
            extracted_questions =extract_questions(file)

        exam_obj =Exam(duration,directory)
        if not extracted_questions or extracted_questions[-1].qtype != 'end':
            return exam_obj, False

        exam_obj.duration = duration  # Set the exam duration
        exam_obj.set_questions(extracted_questions)
        exam_obj.set_exam_status(True)
        exam_obj.shuffle = shuffle  # Set shuffle mode

        return exam_obj, True
    except Exception:
        return None, False

def main(args):
    exam_obj, status = setup_exam()

    if status:
        print("Exam set up successfully.")
    else:
        print("Exam setup failed.")

if __name__ == "__main__":
    main(None)