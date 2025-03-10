import math
from multiprocessing.connection import answer_challenge


def get_range() -> tuple:
    """
    Запрашивает диапазон у пользователя, сортирует, где start - минимальное значение
    end - максимальное значение
    :return: кортеж
    """

    start, end = map(int, input().split())

    start, end = min(start, end), max(start, end)

    return start, end

def validation_range(start, end):
    """
    Проверка диапазона на допустимое значение
    :param start: минимальное значение
    :param end: максимальное значение
    :return: сообщение об успешной проверке
    """

    assert start != end, "Диапазон должен быть валидным (разные числа)"

    return print("Валидный диапазон")

def get_max_attempt(start, end) -> int:
    """
    Высчитывает максимальное кол-во попыток на ответ компьютера
    :param start: Стартовое значение
    :param end: Конечное значение
    :return: Число попыток
    """

    return int(math.log2(end - start)) + 1

def get_ans() -> int:
    """
    Запрашивает ответ пользователя и возвращает в виде int
    :return: число int
    """

    answer = int(input("Загаданное число (больше - 1, меньше - 2, угадал - 3): "))

    return answer



# def game_logic(start, end):
#     """
#     Основное тело игры
#     :param start: Начало диапазона
#     :param end: Конец диапазона
#     :return: none
#     """
#
#     max_attempt: int = get_max_attempt(start, end)
#     attempt: int = 1
#
#     while attempt <= max_attempt:
#         middle: int = (start + end) // 2
#
#         print(f"Ответ компьютера: {middle}")
#         ans = int(input("Загаданное число (больше - 1, меньше - 2, угадал - 3): "))
#
#         answers = ("Больше - 1", "Меньше - 2", "Угадал! - 3")
#         if ans not in answers:
#             print(f"Возможные ответы: {answers} ")
#
#         if ans == 1:  # больше
#             start = middle + 1
#         elif ans == 2:  # меньше
#             end = middle - 1
#         elif ans == 3:
#             print(f"Я угадал! Загаданное число {middle}. Количество попыток: {attempt}")
#             break
#         attempt += 1
