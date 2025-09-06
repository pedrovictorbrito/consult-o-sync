#!/usr/bin/env python3

import sys
import random

def shuffle_file_lines(file_path):
    # Read all lines from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Shuffle the lines
    random.shuffle(lines)

    # Write the shuffled lines back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: shuffle_lines.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    shuffle_file_lines(file_path)
