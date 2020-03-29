num = int(input())
h = num // 100
d = (num / 10) % 10
print(int(h) + int(d) + (num % 10))
