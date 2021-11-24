import re


def url(string: str) -> list:
    # 含括号匹配时不作处理仅返回括号内容
    # 在括号前假设?:后返回所有元素
    result = re.findall(
        r'(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Z\
        a-z0-9+&@#/%=~_|]', string)
    return result


st = url(input())
for i in range(len(st)):
    st[i] = st[i].replace(' ', '')
print(st)
