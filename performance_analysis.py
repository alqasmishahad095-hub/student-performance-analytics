scores = [70, 45, 88, 32]
x = 0
totalStudents = len(scores)

while x < totalStudents:
    if scores[x] % 2 == 0:
        print("Student score is even")
    else:
        print("Student score is odd")
    x = x + 1
