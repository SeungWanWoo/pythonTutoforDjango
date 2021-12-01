'''
Q1
정수 num을 매개변수로 받아 각 자리 숫자(digit)의 합을 계산하는 sumOfDigits() 함수를 작성하세요.
단, 나눗셈을 이용하지 말고 풀어보세요.

'''

def sumOfDigits(num):
    result = 0
    for x in list(str(num)):
        result += int(x)
    return result



if __name__ == '__main__':
    no = input()
    print('문제 1 : ' + sumOfDigits(no))
