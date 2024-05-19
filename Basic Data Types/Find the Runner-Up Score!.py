#github.com/rajendra-patil96
#Python/Basic Data Types/Find the Runner-Up Score!.py

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list = sorted(arr)
    result = [x for x in list if x != max(list)]
    print(result[-1])