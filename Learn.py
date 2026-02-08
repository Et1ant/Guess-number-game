import random

def choose_difficulty():
    """Выбор уровня сложности"""
    print("\nВыберите уровень сложности:")
    print("1 - Легкий (1-50, 10 попыток)")
    print("2 - Средний (1-100, 7 попыток)")
    print("3 - Сложный (1-200, 5 попыток)")
    
    while True:
        choice = input("Введите номер (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        print(" Ошибка! Введите 1, 2 или 3")

def get_difficulty_settings(level):
    """Возвращает настройки для выбранного уровня"""
    settings = {
        1: {'min': 1, 'max': 50, 'attempts': 10, 'name': 'Лёгкий'},
        2: {'min': 1, 'max': 100, 'attempts': 7, 'name': 'Средний'},
        3: {'min': 1, 'max': 200, 'attempts': 5, 'name': 'Сложный'}
    }
    return settings[level]

def get_number_input(min_num, max_num):
    """Безопасный ввод числа с проверкой"""
    while True:
        try:
            num = int(input(f"Введите число от {min_num} до {max_num}: "))
            if min_num <= num <= max_num:
                return num
            print(f"❌ Число должно быть от {min_num} до {max_num}!")
        except ValueError:
            print("❌ Ошибка! Введите целое число.")

def play_game():
    """Основная функция игры"""
    print("=" * 40)
    print(" ИГРА 'УГАДАЙ ЧИСЛО'")
    print("=" * 40)
    
    while True:
        start = input("\nНачать игру? (да/выход): ").strip().lower()
        
        if start == 'выход':
            print("\nСпасибо за игру! До свидания! 👋")
            break
            
        elif start == 'да':
            # Выбор сложности
            level = choose_difficulty()
            settings = get_difficulty_settings(level)
            
            print(f"\n Уровень: {settings['name']}")
            print(f" Диапазон: {settings['min']}-{settings['max']}")
            print(f" Попыток: {settings['attempts']}")
            
            # Генерация числа
            secret_number = random.randint(settings['min'], settings['max'])
            attempts_left = settings['attempts']
            
            print(f"\nЯ загадал число! Попробуйте угадать!")
            
            # Основной игровой цикл
            while attempts_left > 0:
                print(f"\nОсталось попыток: {attempts_left}")
                guess = get_number_input(settings['min'], settings['max'])
                attempts_left -= 1
                
                if guess < secret_number:
                    print(" Ваше число МЕНЬШЕ загаданного")
                elif guess > secret_number:
                    print(" Ваше число БОЛЬШЕ загаданного")
                else:
                    print("=" * 40)
                    print(f" ПОБЕДА! Вы угадали число {secret_number}!")
                    print(f" Использовано попыток: {settings['attempts'] - attempts_left}")
                    print("=" * 40)
                    break
                    
                if attempts_left == 0:
                    print("=" * 40)
                    print(f" Игра окончена! Вы исчерпали все попытки.")
                    print(f" Загаданное число было: {secret_number}")
                    print("=" * 40)
                    break
        else:
            print(" Неверный ввод. Пожалуйста, введите 'да' или 'выход'.")

# Запуск игры
if __name__ == "__main__":
    play_game()

