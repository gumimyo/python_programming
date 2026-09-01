#비트 연산자
a = 5        #0000 0101
b = 3        #0000 0011
print(a & b )#0000 0001
print(a|b)   #0000 0111
print(a^b )  #0000 0110
print(a << b)#5 -> 10 -> 20 -> 40 (*2)
print(40 >> b)#5 <- 10 <- 20 <- 40 (*2)
print(~a)     #1111 1010-> 0000 0110

#멤버십 연산자

print("a" in "apple")
print(3 in [1,2,3])

#삼항 연산자
# int max = a>b ? a : b;
a=2
b=5
max_num = a if a>b else b
print(max_num)

#a가 짝수이면 "even", 홀수면 "odd"
'''
a = int(input(" number :"))

print("even" if a%2 == 0 else "odd")
'''
score = 85
#90이상은 A...
print("A" if score >= 90 else "B" if score >= 80 else "c" if score >= 70 else "D" )

