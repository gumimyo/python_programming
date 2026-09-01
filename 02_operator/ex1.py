#연산자

#산술 연산
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  #몫
print(a%b)
print(a ** b) #거듭제곱

#복합대입 연산자
a +=4
print(a)
a-=10
print(a)

#증감연산자 x

#b=a++
a += 1

#비교연산자

print(3 == 3.0)  #true
print(3 != 4)
print("apple" < "apble")
print(1<2<3)   # 1<2 and 2<3
print(1<3<2)   # and라서 x

#논리 연산자 (and,or,not)
print(True and False)
print(True or False)
print(not True)
#short-circuit test-
a =10
b =0
# print(a/b)

if a> 0 or a/b:
    print("yes")
else:
    print("no")