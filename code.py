num, a, N = 1, {},5
stages = [4, 4, 4, 1, 6]
while num <= N :
    count, counta, z = 0, [], len(stages)

    for i in stages :
        if i == num :
            count += 1

    a[int(num)] = (count/z)
    stages = list(filter(lambda x:x !=num, stages))

    num+=1
    print(a)

a = sorted(a, key=lambda x: a[x], reverse=True)
print(a)