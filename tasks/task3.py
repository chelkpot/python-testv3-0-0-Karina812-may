# tasks/task3.py

def solve():
    # Ниже пишите решение задачи
    n = int(input())
    count = 0
    
    # Берем купюры по 100
    count += n // 100
    n = n % 100
    
    # Берем купюры по 20
    count += n // 20
    n = n % 20
    
    # Берем купюры по 10
    count += n // 10
    n = n % 10
    
    # Берем купюры по 5
    count += n // 5
    n = n % 5
    
    # Берем купюры по 1
    count += n
    
    print(count)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()