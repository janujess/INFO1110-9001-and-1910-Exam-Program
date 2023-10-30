# -*- coding: utf-8 -*-
"""program_two.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wE4mVIxPyc23Ibr5AN01G985wgwABN3Q
"""

from exam import Exam
from setup import extract_students
import program_one

def assign_exam(exam):
    # Extract candidates from the specified students file
    candidates = extract_students(open(candidate_file, "r"))

    if not candidates:
        print("No candidates found in the file.")
        return None

    assigned_candidates = []

    if not exam.shuffle:
        # Non-shuffle mode: Assign the same exam to all candidates
        for candidate in candidates:
            assigned_exam = exam.copy_exam()
            candidate.exam = assigned_exam
            assigned_candidates.append(candidate)
    else:
        # Shuffle mode: Assign randomized exams to candidates
        for candidate in candidates:
            shuffled_exam = exam.copy_exam()
            candidate.exam = shuffled_exam
            assigned_candidates.append(candidate)

    print(f"Assigning exam to candidates... Complete. Exam allocated to {len(assigned_candidates)} candidates.")

    return assigned_candidates

if __name__ == "__main__":
    # Prompt the user to input the directory and students file
    directory = input("Enter the directory path: ")
    candidate_file = input("Enter the name of the students file: ")

    program_one.main(None)  # Call program_one to set up the environment

    # Initialize your exam (replace with your desired exam details)
    exam = Exam(60, directory, shuffle=True)  # Make sure to set shuffle to True or False as needed
    assigned_candidates = assign_exam(exam)

    if assigned_candidates:
        for candidate in assigned_candidates:
            print(f"Candidate: {candidate.name} ({candidate.sid})")
            print(f"Assigned Exam: {candidate.exam.name}")