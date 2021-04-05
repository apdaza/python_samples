#definition of a Z-Combinator
Z = lambda f: (lambda x: f(lambda *args: x(x)(*args)))(lambda x: f(lambda *args: x(x)(*args)))

add = Z(lambda f: lambda a, b: b if a <= 0 else 1 + f(a - 1, b))

print add(1, 1)
print add(8, 2)

factorial = lambda x: 1 if x == 1 else x * factorial (x-1)

print factorial(3)
