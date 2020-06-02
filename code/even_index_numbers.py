# A code to display only numbers from even index and even numbers from new list
def positive(list_1):
    new_list = [list_1[x] for x in range(0, len(list_1), 2) if list_1[x] % 2 == 0]
    print(new_list)


positive([2, 4, 1, 9, 4, 5, 7, 8, 3, 4, 6])
