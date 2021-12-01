"""
Q1
주어진 단어가 회문인지 판별하는 함수 palindrome()을 작성하세요.
단, 문자열 입력은 모두 소문자로 이뤄지며 공백을 포함하지 않는다고 가정합니다.

Q2
대문자와 소문자가 섞여 있더라도 회문으로 판정하도록 함수를 개선하세요.

Q3
공백이 섞여 있더라도 회문으로 판정하도록 함수를 개선하세요.

"""

def palindrome(str):
    """
    if str == str[::-1]:
        return True
    else:
        return False
    """
    return str[:] == str[::-1]

def palindrome2(str):
    return palindrome(str.lower())

def palindrome3(str):
    return palindrome2(str.replace(' ', ''))

if __name__ ==  '__main__':

    for x in ['anna', 'banana', 'Anna', 'My gym']:
        if palindrome3(x):
            print(f"'{x}' is a palindrome")
        else:
            print(f"'{x}' is not a plindrome")
    

