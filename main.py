# Дополнительное практическое задание по модулю 3*

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(structure):
    total = 0

    if isinstance(structure, (list, tuple, set)):
        for item in structure:
            total += calculate_structure_sum(item)

    elif isinstance(structure, dict):
        for key, value in structure.items():
            total += calculate_structure_sum(key)
            total += calculate_structure_sum(value)

    elif isinstance(structure, int):
        total += structure

    elif isinstance(structure, str):
        total += len(structure)

    return total

result = calculate_structure_sum(data_structure)
print(result)

