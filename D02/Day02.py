from time import time

from . import inputData


def run():
    start = time() * 1_000 * 1_000
    total = 0
    for idx, game in enumerate(inputData.inputObj, start=1):
        isValid=True
        maxR = 0
        maxG = 0
        maxB = 0
        for draw in game:
            # if 'r' in draw.keys() and draw['r'] > 12 or \
            #         'g' in draw.keys() and draw['g'] > 13 or \
            #         'b' in draw.keys() and draw['b'] > 14:
            #     isValid = False
            #     break
            # else:
                maxR = draw['r'] if 'r' in draw.keys() and draw['r']>maxR else maxR
                maxG = draw['g'] if 'g' in draw.keys() and draw['g']>maxG else maxG
                maxB = draw['b'] if 'b' in draw.keys() and draw['b']>maxB else maxB
        total += maxR*maxG*maxB if isValid else 0
    end = time() * 1_000 * 1_000
    print(f'time: {end - start}, result: {total}')
