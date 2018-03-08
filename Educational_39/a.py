raw_input()
sum = 0
a = map(int, raw_input().split(' '))
for i in a:
    sum += abs(i)
print sum
