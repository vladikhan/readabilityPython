import math
import re

from cs50 import get_string


# Function to count the number of letters in the text
def count_letters(text):
    count = sum(1 for char in text if char.isalpha())
    return count

# Function to count the number of words in the text


def count_words(text):
    count = len(text.split())
    return count

# Function to count the number of senteces in the text


def count_sentences(text):
    count = len(re.findall(r'[.!?]', text))
    return count


def main():
    # Promt the user for some text
    text = get_string("Your text: ")

    # Count the number of letters, words, and senteces in the text
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculate the Coleman-Liau index
    L = (float(letters) / float(words)) * 100
    S = (float(sentences) / float(words)) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Print the grade level
    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


if __name__ == "__main__":
    main()
