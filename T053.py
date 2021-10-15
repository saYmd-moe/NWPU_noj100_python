import time

while True:
    Date = input()
    if len(Date) == 0:
        break
    else:
        try:
            if '-' in Date:
                time.strptime(Date, "%Y-%m-%d")
                print(True)
            elif '/' in Date:
                time.strptime(Date, "%Y/%m/%d")
                print(True)
            elif '.' in Date:
                time.strptime(Date, "%Y.%m.%d")
                print(True)
        except Exception as e:
            e = 'False'
            print(e)
