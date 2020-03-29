n = int(input())
hour = n % (60 * 24) // 60
mint = n % 60
print(hour, mint)
