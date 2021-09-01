def selectionSort(x):
    for i in range(len(x)):
        min = i
        for j in range(i, len(x)):
            if x[j] < x[min]:
                min = j
        x[i], x[min] = x[min], x[i]
    return x

x = [2, 6, 3, 8, 4, 1]
selectionSort(x)
print(x)