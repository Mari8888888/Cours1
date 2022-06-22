student = []
gpa = []
marks = []
strprogress = ''
with open('dataset_3363_4.txt') as inf:
    for line in inf:
        mark = 0
        student = line.strip().split(';')
        for i in range(1, len(student)):
            mark += int(student[i])
        mark = mark/(len(student) - 1)
        gpa += [mark]
        del student[0]
        marks += [student]
        progress = [0 for i in range(len(student))]
for j in range(0, len(student)):
    for i in range(0, len(marks)):
        progress[j] += int(marks[i][j])
for i in range(len(progress)):
    progress[i] = progress[i]/len(marks)
    strprogress += str(progress[i]) + ' '
with open('dataset_3363_4.txt', 'w') as ouf:
    for i in range(len(gpa)):
        ouf.write(str(gpa[i]) + "\n")
    ouf.write(strprogress)











