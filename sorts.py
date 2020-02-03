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
def bubbleSort(anislist):
    for passnum in range(len(anislist)-1,0,-1):
        for i in range(passnum):
            if anislist[i]>anislist[i+1]:
                temp = anislist[i]
                anislist[i] = anislist[i+1]
                anislist[i+1] = temp
bubbleSort(anislist)
print(anislist)

----------merge sort-----------------
def mergeSort(mollalist):
    print(mollalist)
    if len(mollalist)>1:
        mid = len(mollalist)
        lefthalf = mollalist[:mid]
        righthalf = mollalist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                mollalist[k]=lefthalf[i]
                i=i+1
            else:
                mollalist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            mollalist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            mollalist[k]=righthalf[j]
            j=j+1
            k=k+1
    print(mollalist)
mergeSort(mollalist)
print(mollalist)
-------counting sort----------
def counting_sort(A, max_value):
	    mm = max_value + 1
	    count = [0] * mm                
	    
	    for a in array1:
	    # count occurences
	        count[a] += 1             
	    i = 0
	    for a in range(mm):            
	        for c in range(count[a]):  
	            A[i] = a
	            i += 1
	    return array1
	
	print(counting_sort(A)












