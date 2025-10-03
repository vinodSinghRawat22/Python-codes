# Q8. Create a program to count lines and words in a file.

with open('file8.txt', 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)
    print(f"Number of lines: {line_count}")
    print(f"Number of words: {word_count}")