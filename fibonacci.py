fib = [0, 1]

num = int(input('Informe um número: '))

while(num >= fib[len(fib)-1]):
    fib.append(fib[len(fib)-1] + fib[len(fib)-2])

contido = False

for i in range(len(fib)):
    if(num == fib[i]):
        contido = True

if(contido):
    print('O número pertence a sequência de fibonacci')
else:
    print('O número não pertence a sequência fibonacci')
