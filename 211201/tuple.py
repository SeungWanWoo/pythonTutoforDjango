'''
사용자로부터 날짜를 나타내는 세 개의 숫자를 입력받습니다.
첫 번째 숫자는 연도를 나타내는 네 자리 숫자이고,
두 번째 숫자는 월을, 세 번째 숫자는 일을 나타냅니다.

입력받은 날짜를 mm/dd/yyyy 형식으로 출력합니다.
월을 두 자리 숫자(01, 02, 03, ..., 12)로,
일을 두 자리 숫자(01, 02, 03, ..., 31)로,
연도를 네 자리 숫자로 나타냅니다.

입력받은 날짜의 다음 날에 해당하는 날짜도 같은 형식으로 출력합니다.
단, 윤년은 무시합니다(2월은 항상 28일까지 있다고 가정합니다).
'''
date = input()

y, m, d = tuple(date.split(' '))

_31monthAt = 'N'
_2monthAt = 'N'

def addZero(str):
    if int(str) < 10:
        str = '0' + str
        
    return str

if int(m) == 2:
    _2monthAt = 'Y'
elif (int(m) <= 7) and int(m) % 2 == 1 :
    _31monthAt = 'Y'
elif (int(m) >= 8) and int(m) % 2 == 0:
    _31monthAt = 'Y'


day = addZero(str(d))
month = addZero(str(m))
year = str(y)

if (_2monthAt == 'Y') and int(d) > 27:
    d = 1
    m = int(m) + 1
elif (_31monthAt == 'Y') and int(d) > 30:
    d = 1
    m = int(m) + 1
elif int(d) > 29:
    d = 1
    m = int(m) + 1
else:
    d = int(d) + 1
    
if int(m) > 12:
    m = 1
    y = int(y) + 1
    
tday = addZero(str(d))
tmonth = addZero(str(m))
tyear = str(y)

print(f"today : {month}/{day}/{year}")
print(f"tomorrow : {tmonth}/{tday}/{tyear}")



