"""Игра сама загадывает и угадывает число"""
import numpy as np

def random_predict(number:int=1) -> int:
    count = 0
    
    min, max = 1, 100

    number = np.random.randint(min, max)

    count = 0

    while True:
        count += 1
        mid = (min + max) // 2
        
        if mid > number:
            max = mid
        elif mid < number:
            min = mid
        else:
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