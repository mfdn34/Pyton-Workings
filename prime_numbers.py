
num_limit = input("Enter a limit number: ")

while True:
    if num_limit.isdigit():
        break
    else:
        num_limit = input("Wrong entered. Please enter a limit number: ")

prime_num = []
count = 0

for i in range(2,int(num_limit)+1):
    for j in range(2, i):
        if i % j == 0:
            count = count + 1
            break
    if count == 0:
        prime_num.append(i)
    count = 0

print(prime_num)