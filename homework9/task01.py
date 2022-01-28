"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""


def open_file_and_lines(file_name):
    with open(file_name) as file:
        for line in file:
            yield int(line)


def merge_sorted_files(files_list):
    files_open = [open_file_and_lines(file) for file in files_list]
    numbers = {file_open: next(file_open) for file_open in files_open}
    while True:
        key, min_num = min(numbers.items(), key=lambda x: x[1])
        yield min_num
        try:
            numbers[key] = next(key)
        except StopIteration:
            del numbers[key]
        if not numbers:
            return
