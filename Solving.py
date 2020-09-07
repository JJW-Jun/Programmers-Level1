N, count, counta_ = 5, 1, 0
stages = [2,1,2,6,2,4,3,3]
answers = {}
while count <= N :
    number = len(stages)
    for i in stages :
        if i == count :
            counta_ +=1



        elif i > N :
            answers[i] = 0
        else :
            pass
    answers[count] = counta_/number

    if count in stages :
        list(set(stages)).remove(count)

    print('dd')
    counta_ = 0
    count += 1
import collections
answer = collections.OrderedDict(sorted(answers.items()))
print(answer)