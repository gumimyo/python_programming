# 반복분 : while문 for문
"""
#while문
#1~10까지 반복문 출력
i = 1
while i < 11:
    print(i)
    i += 1
    if i == 5:
        break
else:
    print("end")   # while의 끝까지 도달했을때 출력

nums = [1,3,5,7,9]
target = 2
i = 0
while i < len(nums):
    if nums[i] == target:
        print("found")
        break
    i += 1
else:
    print("not found")

while i <= 10:
    tot += i
    i +=1
else:
    print(tot)
 # (=)
i =1
tot =0
for i in range(1,11):
    tot += i
print(tot)
"""

i = 1
tot = 0
while i <= 10:
    if i % 2 == 0:
        tot += i
    i += 1
else:
    print(tot)
# 홀수일때 건너뛰기
# if i %2 == 1:
#     continue
# tot += i
