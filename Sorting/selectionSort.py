# -------------Basic selection sort--------------
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

#--------------Selection sort by recursion---------------

def min_idx( a , i , j ):
    if i == j: 
        return i
    k = min_idx(a, i + 1, j)
    if a[i] < a[k]:
        return i
    return k
     
def selectionSort_by_recursion(a, n, index = 0):
    if index == n: 
        return -1
    
    k = min_idx(a, index, n-1)
    if k != index:
        a[k], a[index] = a[index], a[k]
    
    selectionSort_by_recursion(a, n, index + 1)
     
# Tester 
arr = [3, 1, 5, 2, 7, 0]
selectionSort_by_recursion(arr, len(arr))
print(arr)