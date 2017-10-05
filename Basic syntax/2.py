from collections import Counter
import os
import sys


def count_words_in_file(filename):
    with open(filename, 'r') as content:
        counter = Counter(content.read().split())
    return counter.most_common(1)[0]

if __name__ == '__main__':
    if not len(sys.argv) >= 2:
        raise AttributeError
    filename = sys.argv[1]
    print(count_words_in_file(filename))
