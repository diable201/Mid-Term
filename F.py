def has_array_two_candidates(A, arr_size, sum):
    # sort the array
    quick_sort(A, 0, arr_size - 1)
    l = 0
    r = arr_size - 1
    # traverse the array for the two elements
    while l < r:
        if A[l] + A[r] == sum:
            return 1
        elif A[l] + A[r] < sum:
            l += 1
        else:
            r -= 1
    return 0


def quick_sort(A, si, ei):
    if si < ei:
        pi = partition(A, si, ei)
        quick_sort(A, si, pi - 1)
        quick_sort(A, pi + 1, ei)

        # Utility function for partitioning the array(used in quick sort)


def partition(A, si, ei):
    x = A[ei]
    i = (si - 1)
    for j in range(si, ei):
        if A[j] <= x:
            i += 1
            # This operation is used to swap two variables is python
            A[i], A[j] = A[j], A[i]
        A[i + 1], A[ei] = A[ei], A[i + 1]

        return i + 1


range_of_list = int(input())
cost = int(input())
my_list = []

for i in range(range_of_list):
    data = int(input())
    my_list.append(data)

if has_array_two_candidates(my_list, len(my_list), cost):
    print('Bon Appetit')
else:
    print('So Sad')

