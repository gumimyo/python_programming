# 자료형
# 1. 기본 자료형: 숫자형(int,float),불리언,문자열(str)
# 2. 컬렉션 자료형: 리스트, 튜플, 딕셔너리, 집합(set)

# 숫자형-정수형 (int)
a = 10
print(a, type(a))

# 2,8,16진수, 아스키 코드
print(bin(a), oct(a), hex(a))
print(ord("A"), chr(65))

# int의 데이터의 표현범위
# 데이터 표현 범위가 없다
x = 10**100
print(x)

# 오버플로우 test => 0
a = 2**31 - 1
print(a)
a = a + 1
print(a)

# 실수형 (float)
b = 3.14
print(b, type(b))

# 실수형의 데이터 표현범위
# 부동 소수점 방식
# 64bit = 부호(1)+지수부(11)+가수부(52)

import sys

print(sys.float_info.min)
print(sys.float_info.max)

print(-sys.float_info.min)
print(-sys.float_info.max)

a = 1.7e308
b = 1.8e308  # (inf)
print(a, b)

# 실수의 오차
print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(f"{0.3:.20f}")

# 형변환
print(float(10))
print(int(3.14))
print(float("3.14"))
print(int("314"))
print(str(10))
