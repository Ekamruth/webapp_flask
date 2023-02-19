# Printing a pattern

N = int(input("Enter n: "))
M = N * 3

n = int((N - 1) / 2)

for i in range(0, n):
    d = int((M - (3 * (i * 2 + 1))) / 2)
    print("-" * d + ".|." * (i * 2 + 1) + "-" * d)

w = int((M - 7) / 2)
print("-" * w + "WELCOME" + "-" * w)

for i in range(n - 1, -1, -1):
    d = int((M - (3 * (i * 2 + 1))) / 2)
    print("-" * d + ".|." * (i * 2 + 1) + "-" * d)
