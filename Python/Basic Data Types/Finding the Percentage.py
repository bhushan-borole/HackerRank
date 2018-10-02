from decimal import Decimal
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list = student_marks[query_name]
    sum = float(0)
    for x in list:
        sum = sum + x
    print(round(Decimal(sum/3),2))