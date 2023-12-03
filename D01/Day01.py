from time import time

from . import inputData as input2
import re


def run():
    start = time() * 1_000 * 1_000
    v = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '': 0,
               '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    nums = '([0-9]|one|two|three|four|five|six|seven|eight|nine)'
    # results = re.findall(r'(?:([0-9]).*([0-9])|([0-9]))',input2.inputVal,re.MULTILINE)
    results = sum(map(lambda x: v[x[0]]*10 + v[x[1]] + v[x[2]]*10 + v[x[2]],
                      re.findall(rf"{nums}\w*{nums}|{nums}", input2.inputVal, re.MULTILINE)))
    end = time() * 1_000 * 1_000
    print(f'time: {end - start}, result: {results}')
