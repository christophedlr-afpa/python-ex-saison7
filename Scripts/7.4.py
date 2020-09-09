val: int
array = [12, 8, 4, 45, 64, 9, 2]

print("Le tableau :")

for i in array:
    print(i)

val = int(input("Choisissez une position dans le tableau : "))

array.pop(val)

print("Le nouveau tableau :")

for i in array:
    print(i)
