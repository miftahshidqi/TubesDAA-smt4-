#!/usr/bin/env python
# coding: utf-8

# In[65]:


print("Merge Sort");
import time
start_time = time.time()
import random

 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #membagi panjang array jadi 2 
        L = arr[:mid] # Array bagian kiri
        R = arr[mid:] # Array bagian kanan
        
        mergeSort(L) # Sorting array pada bagian kiri
        mergeSort(R) # Sorting array pada bagian kanan

        i = j = k = 0
        
        # Copy data array L[] dan R[] ke array arr[]
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        
        # Proses cek agar tidak ada elemen yg tertinggal 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
        
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
        
         
def printList(arr): 
    for i in range(len(arr)):		 
        print(arr[i],end=" ") 
    print() 


#arr = [12, 11, 13, 5, 6, 7] 
arr = [random.randrange(1,1000) for i in range(530)]
print()
print ("Array sebelum di sorting: ", end="\n") 
printList(arr) 
print()
mergeSort(arr) 
print("Array setelah di sorting: ", end="\n") 
printList(arr)

print()
print("--- %s seconds ---" % round(time.time() - start_time, 2))


# In[66]:


print("Buble Sort")

import time
start_time = time.time()
import random

#my_list = [4, -7, 5, 4]
print()
my_list = [random.randrange(1,1000) for i in range(530)]
print ("Array sebelum di sorting: ", end="\n") 
printList(my_list)
print()
is_sorted = False
while not is_sorted:
  is_sorted = True
  for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
      my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
      is_sorted = False

print("Array setelah disorting: ", end="\n") 
printList(my_list) 
print()
print("--- %s seconds ---" % round(time.time() - start_time, 2))


# In[ ]:




