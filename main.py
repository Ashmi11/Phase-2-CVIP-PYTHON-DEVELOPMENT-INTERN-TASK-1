import time

from text_generator import generate_random_text
from typing_speed_tester import run_typing_speed_test
from user_interface import display_text_to_type, get_user_input, display_results

if __name__ == "__main__":
    text_to_type = generate_random_text()
    display_text_to_type(text_to_type)

    start_time = time.time()
    user_input = get_user_input()
    end_time = time.time()

    speed, accuracy = run_typing_speed_test(start_time, end_time, text_to_type, user_input)

    display_results(speed, accuracy)
