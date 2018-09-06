array=[]
for k in range(5):
    a = int(input("Enter number : "))
    b = array.append(a)
    print(array)
    

for j in range(len(array)-1,0,-1):
    for i in range (j):
        if (array[i]>array[i+1]):
            temp=array[i]
            array[i]=array[i+1]
            array[i+1]=temp
alist = array     
print("Sorted Array is : ",alist)
    
