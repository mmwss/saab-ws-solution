"""
Create a Python program that analyzes text files in a given directory and reports
the frequency of each word across all files.
"""

import os
import re
from collections import Counter

def analyze_word_frequency(directory):
    word_count = Counter()
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                words = re.findall(r'\b\w+\b', text)
                word_count.update(words)
    return dict(word_count)

# Example usage
if __name__ == "__main__":
    print("Code Generation[2] Word Frequency Analyzer")

    directory = 'data/frequency'
    frequencies = analyze_word_frequency(directory)
    for word, count in frequencies.items():
        print(f"{word}: {count}")
