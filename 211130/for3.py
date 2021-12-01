L = input('입력 : ').split()
min = int(L[0])
max = int(L[1])

temp = int(input('임시 온도 :'))

while temp != -999:
    if min <= temp <= max:
        print('Nothing to report')
        temp = int(input('임시 온도 : '))
    else:
        print('Alert!')
        break
