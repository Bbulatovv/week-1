a = int(input())
dig1 = a // 1000
dig2 = (a // 100) % 10
dig3 = ((a % 1000) % 100) // 10
dig4 = ((a % 1000) % 100) % 10
if dig1 < dig4:
    print('100000')
elif dig2 < dig3:
    print('1001')
elif dig1 > dig4:
    print('100001')
elif dig2 > dig3:
    print('3535')
else:
    print('1')
