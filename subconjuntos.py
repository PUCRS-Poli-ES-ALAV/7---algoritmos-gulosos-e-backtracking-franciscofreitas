def displaySubset(subSet):
    print("  ".join(map(str, subSet)))

def subsetSum(original_set, current_subset, remaining_elements, total, sum_target):
    if total == sum_target and current_subset and any(x != 0 for x in current_subset):
        displaySubset(current_subset)
        return
    
    for i, elem in enumerate(remaining_elements):
        new_subset = current_subset | {elem}
        new_total = total + elem
        # Sublista sem os elementos anteriores e o atual para evitar repetição
        subsetSum(
            original_set,
            new_subset,
            remaining_elements[i+1:],
            new_total,
            sum_target
        )

def findSubset(original_list, sum_target):
    original_set = set(original_list)
    subsetSum(original_set, set(), original_list, 0, sum_target)

# Exemplo
set_values = [-7, -3, -2, 5, 8]
findSubset(set_values, 0)
