"""Metodo de la burbuja"""
List=[1,5,4,7,8,3,2,9,10,6]
print(List)
for numPast in range(len(List)-1,0,-1):
    for stay in range(numPast):
        if List[stay]>List[stay+1]:
            save = List[stay]
            List[stay] = List[stay+1]
            List[stay+1] = save
            print(List)

print("Otro metodo")
"""Metodo Program for Selection Sort"""
List=[1,5,4,7,8,3,2,9,10,6]
print(List)
for numPast in range(0,len(List),1):
	for check in range(numPast,len(List),1):
		if List[check] == List[numPast]+1:
			save = List[check]
			save2 = List[numPast+1]
			List[numPast+1]=save
			List[check]=save2
			print(List)

print("Otro metodo")

A=[1,5,4,7,8,3,2,9,10,6]
for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
            print(A)
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 

    # Driver code to test above 
print ("Sorted array") 
for i in range(len(A)): 
	print("%d" %A[i]),  