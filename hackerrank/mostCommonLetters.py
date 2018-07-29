# https://www.hackerrank.com/challenges/most-commons/problem

import math
import os
import random
import re
import sys

def formatOutput(result):
    for letter,freq in result[0:3]:
        print(letter + " " + str(freq))

if __name__ == '__main__':
    s = input()
    letters = {}
    for char in s:
        if char in letters.keys():
            letters[char] += 1
        else:
            letters[char] = 1
    sorted_alphabetically = sorted(letters.items(), key=lambda kv: kv[0])
    sorted_by_frequency = sorted(sorted_alphabetically, key=lambda kv: kv[1], reverse = True)
    formatOutput(sorted_by_frequency)
