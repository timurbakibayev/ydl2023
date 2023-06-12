import numpy as np
import timeit


def generate_combinations(n, combination=None, result_combinations=None):
    if combination is None:
        combination = []
    if result_combinations is None:
        result_combinations = []
    if len(combination) == n:
        result_combinations.append(combination)
    else:
        for num in [-1, 0, 1]:
            generate_combinations(n, combination + [num], result_combinations)
    return result_combinations


def generate_combinations2(n):
    results = []
    for i in range(3**n):
        s = np.base_repr(i, base=3)
        s = '0' * (n - len(s)) + s
        results.append([int(c) - 1 for c in s])
    return results


# t1 = timeit.timeit(lambda: generate_combinations(10), number=10)
# t2 = timeit.timeit(lambda: generate_combinations2(10), number=10)
#
# print(t2/t1)
#

print(generate_combinations(3))
