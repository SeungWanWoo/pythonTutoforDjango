while True:
    year = int(input('연도 입력 : '))

    if year % 4 != 0:
        print('평년')
    elif year % 100 != 0:
        print('윤년')
    elif year % 400 != 0:
        print('평년')
    else:
        print('윤년')
