"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
Версия 2. Деление интервала пополам

Автор Иван Клейменов
"""

import numpy as np


def half_interval_predict(number: int = 1) -> int:
    """Угадываем число делением интервала пополам

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1 # устанавливаем счетчик попыток в 1, так как первое предсказание делаем до старта цикла
    min_number = 1 # нижняя граница интервала поиска
    max_number = 100 # верхняя границв интервала поиска
    predict_number = (max_number + min_number) // 2 # делаем первое предсказание
    remainder = 0 # вспомогательный параметр, нужен в случае, когда загаданное число равно max_number 
    

    while predict_number != number:
        count += 1        
        if number > predict_number:
            min_number = predict_number
            remainder = 1 if (max_number + min_number) % 2 != 0 else 0            
        else:   # если загаданное число строго меньше
            max_number = predict_number
            remainder = 0
        
        predict_number = (max_number + min_number) // 2 + remainder   # предполагаемое число
                  
    return count


def score_game(predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(half_interval_predict)



