count = int(input("学生の人数は? "))
student = [0] * count

i = 0
while i < count:
    student[i] = int(input("%d 人目の点数は? " %(i + 1)))
    i += 1

sum = 0
i = 0
while i < count:
    print("%d 人目の点数は %d 点" %(i + 1, student[i]))
    sum += student[i]
    i += 1

print("平均点は %5.1f 点です" %(sum / count))

