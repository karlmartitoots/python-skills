def generator_function():
    yield 1
    yield 2
    yield 3

f = generator_function()
print(next(f))
print(next(f))
print(next(f))

for val in generator_function():
    print(val)