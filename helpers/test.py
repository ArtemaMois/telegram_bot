import datetime
import math

def diffDays():
    startdays = datetime.date(2023, 9, 4)
    nowDay = datetime.date.today()
    diffDay = nowDay - startdays
    if(math.floor((diffDay.days / 7)) % 2 == 0 ):
        return True
    else:
        return False
    
    # return diffDay.days / 7

# res = diffDays()

# startdays = datetime.date(2023, 9, 4)
# nowDay = datetime.date(2023, 9, 8)
# diffDay = nowDay - startdays

# print(diffDay.days/7)

# print(res)

