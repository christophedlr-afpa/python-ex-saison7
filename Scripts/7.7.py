arrayFirst = [10, 42, 84]
arraySecond = [2, 34, 110]
newArray = []
pos: int = 0
temp: int = 0

print("Le premier tableau est : ")
print(arrayFirst)
print("Le second tableau est : ")
print(arraySecond)


for i in range(0, len(arrayFirst)):
    newArray.append(arrayFirst[i])

for i in range(0, len(arraySecond)):
    newArray.append(arraySecond[i])

for x in range(0, len(newArray)):
    for j in range(x, len(newArray)):
        if newArray[j] < newArray[x]:
            pos = j
            temp = newArray[pos]
            newArray[pos] = newArray[x]
            newArray[x] = temp

print("Le troisième tableau est : ")
print(newArray)
