word = []
for i in range (5):
    a = int(input("num :"))
    word.append(a)
print("word =",word)

excel = []
for i in range (5):
    b = int(input("num :"))
    excel.append(b)
print("excel = ",excel)

total = []
for i in range (5):
    c = (word[i]+excel[i])
    total.append(c)
print("total = ",total)
