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
