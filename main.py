import numpy as np
import random

def decreasing(input):
    return sorted(input, reverse=True)

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

def generate_uniform(n):
    return np.random.rand(n)

def generate_cubed(n):
    rand_array = generate_uniform(n)
    return rand_array * rand_array * rand_array

def generate_square_rooted(n):
    rand_array = generate_uniform(n)
    return np.sqrt(rand_array)

def generate_centered(n):
    rand_array = generate_uniform(n)
    for i in range(n):
        rand_array[i] = ((rand_array[i] - 0.5) ** 3) * 4 + 0.5
    return rand_array



if __name__ == '__main__':
    func_list = [first_fit, best_fit, first_fit_decreasing, best_fit_decreasing]
    results = [[], [], [], []]
    for i in range(50):
        input = generate_uniform(100)
        for j in range(4):
            results[j].append(len(func_list[j](input)))
    for j in range(4):
        print(np.mean(results[j]), end=' ')
    print('')

    results = [[], [], [], []]
    for i in range(50):
        input = generate_cubed(100)
        for j in range(4):
            results[j].append(len(func_list[j](input)))
    for j in range(4):
        print(np.mean(results[j]), end=' ')
    print('')

    results = [[], [], [], []]
    for i in range(50):
        input = generate_square_rooted(100)
        for j in range(4):
            results[j].append(len(func_list[j](input)))
    for j in range(4):
        print(np.mean(results[j]), end=' ')
    print('')

    results = [[], [], [], []]
    for i in range(50):
        input = generate_centered(100)
        for j in range(4):
            results[j].append(len(func_list[j](input)))
    for j in range(4):
        print(np.mean(results[j]), end=' ')

    # print(first_fit(input))
    # print(best_fit(input))
    # print(first_fit_decreasing(input))
    # print(best_fit_decreasing(input))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
