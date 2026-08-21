# 변수
a = 2
b = 3
print(a, b)


a = 2;b = 3
a,b = 2,3    #권장
print(a,b)

#값 스왑

# temp = a
# a = b
# b = temp
# print(a, b)  #c

a, b = b, a
print(a,b)

x=y=z = 0

#변수명 작성 규칙 => (c와 동일)
#숫자로 시작x
#예약어는 안됌
#알파벳, 숫자 가능, 특수문자는 _만
#대소문자는 구분한다

한글로변수작성 = "된다"
print(한글로변수작성)  #권장하지 x

student_name = "sss" # snake_case
studentName = "dkdk" # camelCase

MAX_SCORE = 100 #상수로 취금시 대문자로 작성


