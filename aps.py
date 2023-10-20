list = []

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

def heapify(array, n, i):
  maior = i 
  esq = 2 * i + 1 
  dir = 2 * i + 2 

  if esq < n and array[i] < array[esq]:
      maior = esq

  if dir < n and array[maior] < array[dir]:
      maior = dir

  if maior != i:
    (array[i], array[maior]) = (array[maior], array[i]) 
    heapify(array, n, maior) 

def heapSort(array):
  n = len(array) 

  for i in range(n // 2 - 1, -1, -1):
    heapify(array, n, i)

  for i in range(n - 1, 0, -1):
    (array[i], array[0]) = (array[0], array[i]) 
    heapify(array, i, 0) 


with open('1000_numbers.txt') as f:
  list = f.readlines()

for i in range(0, len(list)):
  list[i] = list[i].replace("\n", "")
  list[i] = int(list[i])

print(".")
print("=-"*20 + "INSERTION SORT" + "=-"*20)
insertionSort(list)

print(".")
print("=-"*20 + "BUBBLE SORT" + "=-"*20)
bubbleSort(list)

print(".")
print("=-"*20 + "HEAP SORT" + "=-"*20)
heapSort(list) #Verificar o porque não está dando certo
