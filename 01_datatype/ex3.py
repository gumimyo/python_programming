# 불리언
# true,false

a = True
print(a, type(a))

print(2 < 3)
print(2 > 3)
print(2 == 3)
print(2 != 3)

print("apple" > "banana")  # 사전순
print("apple" < "banana")

# bool()

print(bool(3))  # 모든 0이 아닌 정수는 true
print(bool(0))  # 0dms flase
print(bool("hello"))
print(bool(""))
print(bool([1, 2]))
print(bool([]))

# none 자료형
a = None  # 아직 값이 정해지지 않은 자료형
print(a, type(a))
print(bool(a))

if a is None:
    print("값이 없습니다.")
