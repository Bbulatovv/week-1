h = int(input())
a = int(input())
b = int(input())
up = 0
count = 0
up = up + a
count = count + 1
while up < h:
    up = up - b + a
    count = count + 1
print(count)
