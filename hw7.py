def binary_search(searching_object, list):
    list.sort()

    mid = len(list) // 2

    last = 0

    first = len(list) - 1

    while list[mid] != searching_object and last <= first:

        if searching_object > list[mid]:

            last = mid + 1

        else:

            first = mid - 1

        mid = (last + first) // 2

    if last > first:

        print("Не найдено")

    else:

        print(f"index = {mid}")


binary_search(5, [1, 2, 3, 4])


def bubble_sort(unsorted_list):
    # print(f"your unsorted list: {unsorted_list}")

    for i in range(len(unsorted_list) - 1):

        for k in range(len(unsorted_list) - i - 1):

            if unsorted_list[k] > unsorted_list[k + 1]:
                unsorted_list[k], unsorted_list[k + 1] = unsorted_list[k + 1], unsorted_list[k]

    print(f"Ващ список: {unsorted_list}")

bubble_sort([89, 34, 12, 87, 35])
