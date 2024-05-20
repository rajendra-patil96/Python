#github.com/rajendra-patil96
#Python/Basic Data Types/Nested Lists.py

if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
        
    lowest = sorted(set(scores))[1]    
    nm=[]

    for i,j in records:
        if j==lowest:
            nm.append(i)
    for i in sorted(nm): 
        print(i)