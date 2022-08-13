string = str(input('Digite algo: '))
reverse = ""

print(string)

for i in range(len(string)):
    reverse = reverse + string[len(string) - i - 1]

print(reverse)

