str1 = list(input().split(','))
str2 = list(input().split(','))
str1 += str2
result = {}
for st in str1:
    key_value = st.split(':')
    if key_value[0] in result:
        result[key_value[0]] += int(key_value[1])
    else:
        result[key_value[0]] = int(key_value[1])
print(result)
