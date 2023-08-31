def insertionSort(array):
  for i in range(1, len(array)):
    key = array[i]

    j = i-1
    while j >= 0 and key < array[j]:
      array[j + 1] = array[j]
      array[j] = key
      j -= 1
  print(f'InsertionSort: {array}')

def bubbleSort(array):  
  for i in range(0,len(array)-1): 
    for j in range(len(array)-1): 
      if(array[j]>array[j+1]): 
        key = array[j] 
        array[j] = array[j+1] 
        array[j+1] = key 
  print(f'BubbleSort: {array}')  



ray = [9,3,6,5,1]
print(f"Array Before: {ray}")

insertionSort(ray)
bubbleSort(ray)