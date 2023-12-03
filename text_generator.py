import random

def generate_random_text():
    paragraphs = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is the art of telling another human being what one wants the computer to do.",
        "To be or not to be, that is the question.",
        "In the beginning, God created the heavens and the earth.",
        # Add more sample paragraphs as needed
    ]
    return random.choice(paragraphs)

