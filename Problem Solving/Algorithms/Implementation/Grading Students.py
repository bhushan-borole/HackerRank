# https://www.hackerrank.com/challenges/grading/problem

def grading(grades):
    for x in grades:
        if(x>=38):
            if x%5==0:
                print(x)
                continue
            else:
                next = x + (5-(x%5))
                if(next - x)==3:
                    print(x)
                elif(next - x)<3:
                    print(next)
                else:
                    print(x)
        else:
            print(x)
            

if __name__ == '__main__':
    n = int(input())
    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)
        
    grading(grades)
