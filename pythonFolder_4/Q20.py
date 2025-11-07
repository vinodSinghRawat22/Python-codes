# 20. Write a Python program to count how many sentences are in a paragraph.

import re

paragraph = input("Enter paragraph: ")

sentences = re.split(r'[.!?]', paragraph)
sentences = [s.split() for s in  sentences if s.strip()!= ""]

sentence_count = len(sentences)

print(f"The paragraph contains {sentence_count} sentences.")