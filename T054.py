def MinIndex(List):
    minindex = 0
    currentindex = 1
    while currentindex < len(List):
        if List[currentindex] < List[minindex]:
            minindex = currentindex
        currentindex += 1
    return minindex


def MaxIndex(List):
    maxindex = 0
    currentindex = 1
    while currentindex < len(List):
        if List[currentindex] > List[maxindex]:
            maxindex = currentindex
        currentindex += 1
    return maxindex


sentence = input().split()
length = len(sentence)
i = 0
LengthList = []
while i < length:
    LengthList.append(len(sentence[i]))
    i += 1
print(sentence[MinIndex(LengthList)])
print(sentence[MaxIndex(LengthList)])
