import utils

def main():
    print("Введите начало и конец диапазона загаданного числа: ", end="")
    start, end = utils.get_range()

    utils.validation_range(start, end)

    max_attempt: int = utils.get_max_attempt(start, end)
    attempt: int = 1

    while attempt <= max_attempt:
        middle: int = (start + end) // 2

        print(f"Ответ компьютера: {middle}")
        ans = utils.get_ans()
        answers = ("Больше - 1", "Меньше - 2", "Угадал! - 3")

        if ans not in answers:
            print(f"Возможные ответы: {answers} ")

        if ans == 1:  # больше
            start = middle + 1
        elif ans == 2:  # меньше
            end = middle - 1
        elif ans == 3:
            print(f"Я угадал! Загаданное число {middle}. Количество попыток: {attempt}")
            break
        attempt += 1


if __name__ == "__main__":
    main()