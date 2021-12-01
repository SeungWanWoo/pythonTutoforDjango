from datetime import datetime
today = datetime.today()
today

def __age__(year):
    return today.year - year + 1

print(__age__(int(input('년도 : '))))

