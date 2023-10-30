\# Test Plan for mark_response Method

\## Test Cases - \`test_mark_response_single_correct\`:  - Description:
Test when the question type is \'single\' and the response is correct.
 - Input: Correct answer \'A\', Response \'A\'  - Expected Output: Marks
should be 1.0

\- \`test_mark_response_single_incorrect\`:  - Description: Test when
the question type is \'single\' and the response is incorrect.  - Input:
Correct answer \'B\', Response \'A\'  - Expected Output: Marks should be
0.0

\- \`test_mark_response_multiple_all_correct\`:  - Description: Test
when the question type is \'multiple\' and all responses are correct.  -
Input: Correct answer \'A, B, C\', Response \'A, B, C\'  - Expected
Output: Marks should be 1.0

\- \`test_mark_response_multiple_partial_correct\`:  - Description: Test
when the question type is \'multiple\' and some responses are correct.
 - Input: Correct answer \'A, B, C\', Response \'A, C\'  - Expected
Output: Marks should be approximately 0.67 (rounded to 2 decimal places)

\- \`test_mark_response_multiple_incorrect\`:  - Description: Test when
the question type is \'multiple\' and the response is completely
incorrect.  - Input: Correct answer \'A, B, C\', Response \'D\'  -
Expected Output: Marks should be 0.0

\- \`test_mark_response_type_short\`:  - Description: Test when the
question type is \'short\'.  - Input: Response for short-answer type
question.  - Expected Output: Marks should be 0.0

\## Running the Tests 1. Run \`python test_program.py\`. 2. Observe the
test results for each test case.
