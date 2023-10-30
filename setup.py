# -*- coding: utf-8 -*-
"""setup.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HT38JPhEsvNTUdzZ5rmMQF-fLEB1RBea
"""

from candidate import Candidate
from question import Question
def extract_questions(file):
    questions = []
    current_question = None

    for line in file:
        line = line.strip()
        if line.startswith("Question - "):
            # Extract the question type
            question_type = line[len("Question - "):]
            current_question = Ques.Question(question_type)

        elif line.startswith("Expected Answer: "):
            # Set the correct answer for the current question
            correct_answer = line[len("Expected Answer: "):]
            if current_question:
                current_question.set_correct_answer(correct_answer)

        elif line.startswith("Marks: "):
            # Set the marks for the current question
            marks = int(line[len("Marks: "):])
            if current_question:
                current_question.set_marks(marks)

        elif line.startswith("Possible Answers:"):
            # Process answer options
            answer_options = []
            for _ in range(4):
                answer = file.readline().strip()
                if answer.startswith("A. ") or answer.startswith("B. ") or answer.startswith("C. ") or answer.startswith("D. "):
                    is_correct = answer.endswith(" (correct)")
                    answer = answer[:2]
                    answer_options.append((answer, is_correct))
            if current_question:
                current_question.set_answer_options(answer_options)

        elif line:
            # Accumulate the question description
            if current_question:
                current_question.description += line + "\n"

        elif current_question:
            # Add the current question to the list
            questions.append(current_question)
            current_question = None

    # Add an "end" question to indicate the end of the exam
    questions.append(Ques.Question("end"))

    return questions

# Example usage:
if __name__ == "__main__":
    with open("questions.txt", "r") as file:
        extracted_questions = extract_questions(file)

    for i, question in enumerate(extracted_questions):
        print(question.preview_question(i + 1))

def sort(input_list, order):
    # Check if the order is valid (0, 1, or 2)
    if order not in (0, 1, 2):
        return input_list[:]  # Return a new list with the original data

    # Custom sorting function for ascending order
    def ascending_sort(arr):
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    # Custom sorting function for descending order
    def descending_sort(arr):
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    # Return a new list based on the specified order
    if order == 0:
        return input_list[:]  # No sorting, return a new list
    elif order == 1:
        return ascending_sort(input_list[:])  # Ascending order
    elif order == 2:
        return descending_sort(input_list[:])  # Descending order

    # Invalid order, return a new list
    return input_list[:]

# Example usage:
my_list = [5, 2, 8, 1, 9, 3]
sorted_list = sort(my_list, 1)  # Sort in ascending order
print(sorted_list)  # Output: [1, 2, 3, 5, 8, 9]