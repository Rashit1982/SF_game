"""Игра сама загадывает и угадывает число"""
import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number_up_to_100 = np.random.randint(91, 101)
        predict_number_up_to_90 = np.random.randint(76, 91)
        predict_number_up_to_75 = np.random.randint(61, 76)
        predict_number_up_to_60 = np.random.randint(46, 61)
        predict_number_up_to_45 = np.random.randint(31, 46)
        predict_number_up_to_30 = np.random.randint(16, 31)
        predict_number_up_to_15 = np.random.randint(1, 16)
        if number <= 15:
            if number == predict_number_up_to_15:
                break
        if 16 <= number <= 30:
            if number == predict_number_up_to_30:
                break
        if 31 <= number <= 45:
            if number == predict_number_up_to_45:
                break
        if 46 <= number <= 60:
            if number == predict_number_up_to_60:
                break
        if 61 <= number <= 75:
            if number == predict_number_up_to_75:
                break
        if 76 <= number <= 90:
            if number == predict_number_up_to_90:
                break
        if number >= 91:
            if number == predict_number_up_to_100:
                break
    return(count)

print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количсетво попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = (1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадываает число в среднем за: {score} попыток')
    
    return(score)
if __name__=='__main__':
    score_game(random_predict)