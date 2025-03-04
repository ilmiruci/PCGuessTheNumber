import math

print("Введите начало и конец диапазона загаданного числа: ", end="")
start, end = map(int, input().split())

start, end = min(start, end), max(start, end)

assert start != end, "Диапазон должен быть валидным (разные числа)"

print("Валидный диапазон")

max_attempt:int = int(math.log2(end - start)) + 1
attempt: int = 1

while attempt <= max_attempt:
    middle: int = (start + end) // 2

    print(f"Ответ компьютера: {middle}")
    ans = int(input("Загаданное число (больше - 1, меньше - 2, угадал - 3): "))

    answers = ("Больше - 1", "Меньше - 2", "Угадал! - 3")
    if ans not in answers:
        print(f"Возможные ответы: {answers} ")

    if ans == 1: # больше
        start = middle + 1
    elif ans == 2: # меньше
        end = middle - 1
    elif ans == 3:
        print(f"Я угадал! Загаданное число {middle}. Количество попыток: {attempt}")
        break
    attempt += 1

