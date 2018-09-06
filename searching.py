array=[]
for i in range(5):
    a = int(input("Enter num : "))
    b = array.append(a)
    print(array)

c = int(input("search num : "))
for i in range(5):
    if (array[i]==c):
        print("number is found. Index is :", i)

    
