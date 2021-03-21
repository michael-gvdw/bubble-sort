# bubble sort project

# bubble sort with for loop
def bubble_sort_for(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr


def bubble_sort_while(arr):
    i = 0
    is_sorted = False
    while not is_sorted and i < len(arr):
        is_sorted = True
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                is_sorted = False
        i += 1
    return arr


if __name__ == '__main__':
    val1 = bubble_sort_for([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])

    print(val1)
    val2 = bubble_sort_while([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])
    print(val2)
