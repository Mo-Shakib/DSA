
# ---------- resizing an circular array without changing the starting index of circular array-------------

# def resize(circ,start,size):
#     resizedCirc = [0]*(len(circ)+2) # 2 added here because we are increasing the size of the array by 2
#     index_circ = start
#     index_resizedCirc = start

#     i = 0
#     while(i < size):
#         resizedCirc[index_resizedCirc] = circ[index_circ]
#         index_circ = (index_circ+1)%len(circ)
#         index_resizedCirc = (index_resizedCirc+1)%len(resizedCirc)
#         i = i+1

#     return resizedCirc

# circ=[20,30,40,50,10] #creating a circular array with start 4 and size 5
# circ=resize(circ,4,5)
# print(circ)

# Output: [40, 50, 0, 0, 10, 20, 30] by increasing the size by 2

# ---------------------END------------------------

# -----------------Creating an circular array from an liner array-------------------

# def linToCir(arr,startingIndex):
#     cir = [0]*len(arr)
#     index = startingIndex

#     for i in range(len(arr)):
#         cir[index] = arr[i]
#         index = (index+1)%len(arr)
#     return cir

# lin = [10, 20, 30, 0, 0]
# cir = linToCir(lin, 2) # starting index 2 means that the new array's 1st element will the the index element
# print(f'Linier array: {lin}')
# print(f'Circular array: {cir}\nStarting index: 2')

# -------------------------END----------------------------

# Inserting an Element at the end of a circular array - x

# def insert(cir, start, size, item):
#     if size < len(cir):
#         index = (start+size)%len(cir)
#         cir[index] = item
#         size += 1
#     else:
#         newCir = [0]*(len(cir)+2)
#         x = start
#         st = start
#         i = 0

#         while i < size:
#             newCir[x] = cir[st]
#             x = (x+1)%len(newCir)
#             st = (st+1)%len(cir)
#             i += 1

#         cir = newCir
#         ind = (start+size)%len(cir)
#         cir[ind] = item
#         size += 1
#         return newCir


# a = [4, 5, 1, 2, 3]
# b = insert(a, 2, 7, 6)
# print(b)

# ----------------------------END------------------------

# Inserting an element in a circular array without changing the starting index

# def insertatlast(list, start, size, value ):
#     i = 0
#     index = start
#     while i < size:
#         index = (index+size-1)%len(list)
#         i += 1

#     # So now index in last postion
#     list[index+1] = value
#     return list

# print(insertatlast([1,2,0,0,0,3,4,5], 5, 5, 100))

# ------------reversing an array: in place------------

# def reverse(source):
#     i=0 #pointer at 0th index of source
#     j=len(source)-1 #pointer at last index of source
#     while(i<j):
#         temp=source[i] #swapping the first and last elements
#         source[i]=source[j]
#         source[j]=temp

#         i=i+1
#         j=j-1

# a=[10,20,30,40,50]
# reverse(a)
# print(a)

# -------------------reversing an array: out of place----------------------

# def reverse(source):
#     dest=[0]*len(source)  #creating an empty array named dest having the same length as source
#     i=0 #pointer at 0th index of source
#     j=len(dest)-1 #pointer at last index of dest

#     while(i<len(source)):
#         dest[j]=source[i] #copying element from source to dest
#         i=i+1
#         j=j-1
#     return dest #returning the array containing the elements in reverse order

# a=[10,20,30,40,50]
# b=reverse(a)
# print(b)

# --------------right rotating an array by one place---------------------

# def rightRotate(source):
#     temp=source[len(source)-1] #copying the last element of the array in temp
#     i=len(source)-1 #pointer at last index of source

#     while(i>=1):
#         source[i]=source[i-1] #shifting elements to the right
#         i=i-1
#     source[0]=temp #copying the last element of the array in the 0th index

# a=[10,20,30,40,50]
# rightRotate(a)
# print(a)


# --------------right shifting an array by k places---------------

# def rightShift(source,k):
#     i=len(source)-1 #pointer at the last index of source
#     while(i>=k):
#         source[i]=source[i-k]  #shifting elements k places to the right
#         i=i-1

#     i=0
#     while(i<k):
#         source[i]=0 #setting first k values to 0
#         i=i+1

# a=[10,20,30,40,50]
# rightShift(a,3)
# print(a)

# ---------------- a methord to left rotating an array by k place-------------
# def left_rotate(arr, d):
#     n = len(arr)
#     for i in range(d):
#         temp = arr[0]
#         for j in range(n-1):
#             arr[j] = arr[j+1]
#         arr[n-1] = temp
#     return arr

# a = [1,2,3,4,5]
# b = left_rotate(a, 2)
# print(b)

# ---------------- Insert an tem in a array at k index------------------------
# def insert(a, index, value, size):
#     if size == len(a):
#         print('No more space')
#         return
#     if index < 0 or index > size:
#         print('Wrong index')
#         return
#     i = size - 1
#     while i >= index:
#         a[i+1] = a[i]
#         i -= 1
#     a[index] = value

# source = [10, 20, 30, 40, 50, 0, 0, 0]
# insert(source, 2, 200, 5)
# print(source)
# -----------------------------------------------------


# -----------------forward printing a circular array-----------
# def printForward(c,start,size):
#     index=start
#     i=0
#     while(i<size):
#         print(c[index], end=' ')
#         index=(index+1)%len(c)
#         i=i+1

# circularArray=[40,50,0,0,0,0,0,0,10,20,30] #creating a circular array with start 8 and size 5
# printForward(circularArray,8,5)

# ----------------reverse printing a circular array-------------

def printReverse(c, start, size):
    index = (start+size-1) % len(c)

    i = 0
    while(i < size):
        print(c[index], end=' ')
        index = index-1
        if(index < 0):
            index = len(c)-1
        i = i+1


# creating a circular array with start 8 and size 5
circularArray = [40, 50, 0, 0, 0, 0, 0, 0, 10, 20, 30]
printReverse(circularArray, 8, 5)
