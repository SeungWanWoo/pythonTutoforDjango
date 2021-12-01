'''
십진수를 입력받아 그 숫자에 해당하는 이진수의 각 자리를
리스트로 출력하는 프로그램을 작성하세요. (순서에 유의)
'''
def binary(num):
    binaryList = []

    while True:
        if num == 0:
            break
        
        binaryList.append(num % 2)
        num = num // 2
    
    print(binaryList[::-1])

def answer(d):
    m = d
    b = []

    while True:
        d, m = divmod(d, 2)
        b.insert(0, m)
        if (d == 0):
            break

    print(b)

if __name__ == '__main__':
    num = int(input())
    binary(num)
    answer(num)
