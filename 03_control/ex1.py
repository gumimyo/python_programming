# 조건문 : if문 ,matcha문

age = 16
if age >= 18:
    print("성년")
else:
    print("미성년")
score = 85


if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("c")

#mac-tch

grade = "A"

match grade:
    case "A":
        print("gooood")     #자동 브레이크
    case "B":
        print("good")
    case "C" | "D":
        print("not bad")
    case _:
        print("I think you have to check your score")


