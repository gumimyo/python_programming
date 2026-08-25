# 문자열(str)
#'',""

a = "python"
print(a, type(a))

print("I'll be back")
print("I'll be back")

# 여러줄 문자열

a = """
life is short
You need python
"""
print(a)


def func():
    """#첫번째 줄부터 써야 효력이 있음
    func() 함수에 대한 설명 ~~
    """
    print("hello")
    pass


print(func.__doc__)
print(func())

# 여러줄 주석
"""
이것은 주석이다

"""

# 문자열 연결
print("hello" + " world")

# 문자열 반복
print("hello " * 10)
print("-" * 50)  # 구분선 만들기

# print("hello"+10) 더하기는 같은 자료형끼리만 가능
print("hello" + str(10))

print("10" + "2")  # 102
print(int("10") + int("2"))  # 12

# 문자열 포맷팅 (f - string)
name = "pororo"
age = 23

print(f"{name}의 나이는 {age}살")
print(f"{name}의 다음 내년 나이는 {age+1}살")
print(f"{name.upper()}")  # 함수도 가능

pi = 3.141592
print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}")
print(f"{num:15,d}")
print(f"{num:<15,d}")
print(f"{num:015,d}")
# dlwjdehdml ehsdl dlTdmaus whgrpTek
