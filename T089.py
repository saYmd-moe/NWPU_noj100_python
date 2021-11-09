class RomanNum():
    def __init__(self, RN):
        self.RN = RN

    def ArabicNum(self):
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        AN = 0
        for i in range(len(self.RN) - 1):
            if dic[self.RN[i]] < dic[self.RN[i + 1]]:
                AN -= dic[self.RN[i]]
            else:
                AN += dic[self.RN[i]]
        AN += dic[self.RN[len(self.RN) - 1]]
        return AN if 1 < AN < 3999 else False


RN = RomanNum(input())
print(RN.ArabicNum())
