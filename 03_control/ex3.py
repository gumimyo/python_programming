# #for 문

# # for (int i =0; i <= 10; i++)

# #python => for i in iterable객체:

# for i in range(5):
#     print(i,end = " ")
# print()

# a = range(5)
# print(a.start,a.stop,a.step)

# for i in range(1,6):
#     print(i,end = " ")
# print()

# for i in range(0,11,2):
#     print(i,end = " ")
# print()

# for i in range(5,0,-1):
#     print(i,end = " ")
# print()

# tot = 0
# for i in range(1,11):
#     tot += i
# else:
#     print(tot)

# print(sum(range(1,11)))

# s = "hi12&@한글"

# for c in s:
#     print(c,end=" ")

# print(len(s))

#구구단
for i in range(2,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j:<5d}", end = "\t ")
    print()

