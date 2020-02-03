--------------insertion sort------------------
def insertionSort(A):
  length=len(A)

  for j in range(1,length):
    key=A[j]
    i=j-1
    while i>-1 and A[i]>key:
      A[i+1]=A[i]
      i=i-1
    A[i+1]=key

  print(A)


------------selection Sort--------------
def selectionSort(plist):
   for fillslot in range(len(plist)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if plist[location]>plist[maxpos]:
               maxpos = location

       temp = plist[fillslot]
       plist[fillslot] = plist[maxpos]
       plist[maxpos] = temp
selectionSort(plist)
print(plist

--------------bubble sort--------------
def bubbleSort(mylist):
    for j in range(len(mylist)-1,0,-1):
        for i in range(j):
            if mylist[i]>mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp

mylist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(mylist)

----------merge sort-----------------
def mergeSort(nlist):
   
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
   

mergeSort(nlist)
print(nlist)

-------counting sort----------
def countingSort(array1):
    size = len(array1)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[array1[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[array1[i]] - 1] = array1[i]
        count[array1[i]] -= 1
        i -= 1
    for i in range(0, size):
        array1[i] = output[i]
array2 = [4, 2, 2, 8, 3, 3, 1]
countingSort(array2)

print(array2)








