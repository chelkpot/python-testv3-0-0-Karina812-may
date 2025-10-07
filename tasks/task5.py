# tasks/task5.py

def solve():
    # Ниже пишите решение задачи
    n = int(input())
    
    # Находим часы, минуты и секунды
    hours = n // 3600
    minutes = (n % 3600) // 60
    seconds = n % 60
    
    # Форматируем вывод с ведущими нулями для минут и секунд
    print(f"{hours}:{minutes:02d}:{seconds:02d}")

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()