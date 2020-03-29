hour1 = int(input())
min1 = int(input())
sec1 = int(input())
hour2 = int(input())
min2 = int(input())
sec2 = int(input())
hourTotal = (hour2 - hour1) * 3600
minTotal = (min2 - min1) * 60
secTotal = (sec2 - sec1)
solution = hourTotal + minTotal + secTotal
print(solution)
