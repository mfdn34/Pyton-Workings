fruits = ['Banana\n', 'Orange\n', 'Apple\n', 'Strawberry\n', 'Cherry\n']

with open("fruits.txt","w",encoding="utf-8") as file:
    file.writelines(fruits)

with open("fruits.txt","r",encoding="utf-8") as file:
    print(file.read())

with open("fruits.txt","a",encoding="utf-8") as file:
    file.write("melon")

file = open("fruits.txt","r",encoding="utf-8")
print(file.read())
file.close()