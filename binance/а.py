import math

x = 0.3
d = -0.01
q = 1.1
n = 2

a = math.asin(x) * 0.5

if a <= 0.1 or a == 2:
    y = math.cos(x) + math.sin(x)
elif 0.1 < a < 0.2 or a == 1:
    y = q ** n * math.sqrt(abs(x))
else:
    y = (math.e ** (2 * x)) * math.sqrt(d ** 2 + 1)

print(f'Значение a = {a}.')
print(f'Значение y = {y}.')