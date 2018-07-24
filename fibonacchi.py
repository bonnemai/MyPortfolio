def fib(n):
    if n<2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


print(fib(5))
for i in range(1, 10):
    print(str(i) + ' '+ str(fib(i)))

def factorial(n):
    if n<=1:
        return 1
    return n * factorial(n-1)

print('-------------')

for i in range(1, 10):
    print(str(i) + ' '+ str(factorial(i)))