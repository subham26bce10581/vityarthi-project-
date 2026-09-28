
Cse Project: Triple-Test Jaundice Classifier

This Python program implements a simple three-tiered classification system to meet the following CSE syllabus requirements:

Syllabus Compliance

Requirement

Implementation

Functions

Three distinct functions for Input, Processing, and Reporting.

Dictionary

Used for defining classification levels and passing data between modules.

Control Flow

if/elif/else used to implement the tiered classification logic.

Goal

Provides a prediction/classification based on multiple inputs.

Classification Rules (Prediction/Classification)

The system counts the number of positive ('yes') results from three tests and assigns a risk level:

3 Positive Tests: CONFIRMED Jaundice (Highest Risk)

2 Positive Tests: MODERATE CHANCE Jaundice (Middle Risk)

1 or 0 Positive Tests: LEAST CHANCE Jaundice(Lowest Risk)

Execution Instructions

Save the file as classifier_final.py.

Run the file using the Python interpreter (e.g., in your PyCharm Terminal):

python classifier_final.py


The program will prompt you for the Patient ID and three subsequent 'yes/no' answers.
