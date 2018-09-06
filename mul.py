array = []
for i in range (5):
    a = int(input("Enter num : "))
    array.append(a)
    print(array)

if (array[i]>array[i+1]):
    temp=array[i]
    array[i]=array[i+1]
    array[i+1]=temp
    print(array)

