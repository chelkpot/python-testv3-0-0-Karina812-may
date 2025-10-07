# tasks/task1.py

def solve():
    # Ниже пишите решение задачи
    n = int(input())
    a = n//100
    b = (n//10)%10
    c = n%10
    print(a+b+c)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()