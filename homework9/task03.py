"""Task 3.

Write a function that takes directory path,
a file extension and an optional tokenizer.
It will count lines in all files with that
extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
"""


def universal_file_counter(dir_path, file_extension, tokenizer=None):
    count = 0
    for file in dir_path.glob("*." + file_extension):
        with open(file) as f:
            count += sum(len(tokenizer(line))
                         if tokenizer else 1 for line in f)
    return count
