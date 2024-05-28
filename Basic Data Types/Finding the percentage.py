#github.com/rajendra-patil96
#Python/Basic Data Types/Finding the percentage.py

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores = student_marks[query_name]
    total_sum = sum(scores)
    average = total_sum / len(scores)
    print(f"{average:.2f}")