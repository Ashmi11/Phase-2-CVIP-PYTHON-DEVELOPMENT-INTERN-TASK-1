Purpose: 
The Typing Speed Tester is a Python application designed to help users practice their typing skills. 
It generates random text for users to type, calculates their typing speed in words per minute (WPM),
and provides feedback on typing accuracy.

text_generator module: This module contains a function generate_random_text() that returns a randomly chosen paragraph 
from a list of sample paragraphs. The purpose is to provide a random text for the user to type during the typing speed 
test.

typing_speed_tester module: This module contains functions for calculating typing speed and accuracy.
calculate_typing_speed calculates the typing speed in words per minute (WPM) based on the time taken and the number of
words typed. calculate_typing_accuracy calculates the typing accuracy by comparing the original and typed texts.
run_typing_speed_test combines these functions and returns the calculated speed and accuracy.

user_interface module: This module contains functions for handling user input and displaying information.
get_user_input prompts the user to type the given text.
display_text_to_type prints the text for the user to type.
display_results prints the calculated typing speed and accuracy.

main module: This is the main script.
It imports functions from other modules and executes them in a sequence to generate random text, display it to the user, 
collect user input, calculate typing speed and accuracy, and finally display the results.


How to Run

Clone the Repository:

git clone https://github.com/your-username/typing-speed-tester.git
cd typing-speed-tester


Install Dependencies:
The application does not have external dependencies beyond the standard Python libraries. 
Ensure you have Python 3 installed on your system.

Run the Application:
python main.py
This command will start the application. Follow the on-screen instructions to complete the typing test.

Usage

Text Display:
The application displays a random text that the user needs to type.

User Input:
Type the given text as accurately and quickly as possible.

Results:
After completing the typing, the application will display the typing speed in WPM and typing accuracy as a percentage
