scores = [70, 45, 88, 32]
x = 0
totalStudents = len(scores)

while x < totalStudents:
    if scores[x] % 2 == 0:
        if scores[x] >= 50:
            print("Student score is even and pass")
        else:
            print("Student score is even but fail")
    else:
        print("Student score is odd")
    x = x + 1

