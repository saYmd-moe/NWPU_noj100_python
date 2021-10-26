from copy import deepcopy


def recursion(dic, resultdic, i):
    dic[i] = resultdic


ls = input().split(' ')
ls.reverse()
resultdic = {}
dic = {}

for i in ls:
    recursion(dic, resultdic, i)
    resultdic = deepcopy(dic)
    dic = {}

print(resultdic)
