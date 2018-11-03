# example from (Slattkin 2016, p. 34)
#
# Slatkin, Brett: Effective Python, 4th edition, Pearson Edication Inc., 2016
# 
# usage (for checking example code correctness):
# numbers = [8, 3, 1, 2, 5, 4, 7, 6]
# group = {2, 3, 5, 7}
# sort_priority3(numbers, group)
# print(numbers)
# [2, 3, 5, 7, 1, 4, 6, 8]

def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=sorted)
    return found
