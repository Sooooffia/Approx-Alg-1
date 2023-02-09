import numpy as np
import random

def decreasing(input):
    input.sort()

'''
input style: a list of objects with only weights (no numbering)
'''
def first_fit(input):
    output = [[1]]
    for item in input:
        ind = 0
        for bin in output:
            if bin[0] >= item:
                bin.append(item)
                bin[0] -= item
                ind = 1
                break
        if ind == 0:
            output.append([1-item,item])
    return output

def best_fit(input):
    output = [[1]]
    for item in input:
        ind = 0
        best = [1]
        for bin in output:
            temp = bin[0]
            if  temp - item >= 0 and temp <= best[0]:
                best = bin
                ind = 1
        if ind == 1:
            output[output.index(best)].append(item)
            output[output.index(best)][0] -= item
        else:
            output.append([1 - item, item])
    return output

def first_fit_decreasing(input):
    return first_fit(decreasing(input))

def best_fit_decreasing(input):
    return best_fit(decreasing(input))

def generate_random(n):
    return np.random.randint(1, 101, n) / 100;


if __name__ == '__main__':
    input = generate_random(10)
    print(first_fit(input))
    print(best_fit(input))
    print(first_fit_decreasing(input))
    print(best_fit_decreasing(input))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
