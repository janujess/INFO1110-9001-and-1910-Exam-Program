# -*- coding: utf-8 -*-
"""candidate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UdAp9eiJsM6Es0XAvoeok2dBuEXzhiYc
"""

class Candidate:
    def __init__(self, sid, name, extra_time=0):
        self.sid = sid
        self.name = name
        self.extra_time = extra_time
        self.exam = None
        self.confirm_details = False
        self.results = []

    def get_duration(self):
        if self.exam:
            return self.exam.duration + self.extra_time
        else:
            return 0

    def edit_sid(self, new_sid):
        if isinstance(new_sid, str) and new_sid.isnumeric() and len(new_sid) == 9:
            self.sid = new_sid

    def edit_extra_time(self, extra_time):
        if isinstance(extra_time, int) and extra_time >= 0:
            self.extra_time = extra_time

    def set_confirm_details(self, sid, name):
        if self.sid == sid and self.name == name:
            self.confirm_details = True

    def set_results(self, results):
        if self.confirm_details and self.exam:
            if len(results) == len(self.exam.questions) - 1:  # Exclude the end question
                self.results = results

    def do_exam(self, preview=False):
        if self.exam:
            print(f"Candidate: {self.name}({self.sid})")
            print(f"Exam duration: {self.get_duration()} minutes")
            print(f"You have {self.get_duration()} minutes to complete the exam.")

            if preview:
                # Display exam content for preview
                print(self.exam.preview_exam(self))
            else:
                # Administer the exam
                for question_number, question in enumerate(self.exam.questions, start=1):
                    print(question.preview_question(question_number))

                    if question.qtype == "single":
                        # For single-choice questions, validate and get response
                        response = input("Enter your response (A, B, C, or D): ").strip().upper()
                        if response not in ["A", "B", "C", "D"]:
                            response = "Invalid"  # Mark as invalid if response is not A, B, C, or D

                    elif question.qtype == "multiple":
                        # For multiple-choice questions, validate and get response
                        valid_options = ["A", "B", "C", "D"]
                        response = input("Enter your responses (e.g., A, B, C): ").strip().upper()
                        response = ",".join([opt for opt in response.split(",") if opt in valid_options])

                    else:
                        # Handle short answer questions (no validation)
                        response = input("Enter your response: ").strip()

                    # Mark the response and log the attempt
                    marks = question.mark_response(response)
                    self.log_attempt(question_number, response, marks)

        # End of the exam
        print("Exam completed. Your responses have been saved.")

# Add this method to the Candidate class


    def log_attempt(self, question_number, response, marks):
        if self.confirm_details and self.exam:
            # Generate the filename with the candidate's SID
            filename = f"{self.sid}.txt"

            # Open the file in append mode to log attempts
            with open(filename, "a") as attempt_file:
                attempt_file.write(f"Question {question_number}:\n")
                attempt_file.write(f"Response: {response}\n")
                attempt_file.write(f"Marks: {marks}\n\n")