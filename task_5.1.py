"""
Решение влоб, через рекурсивную функцию, скорей всего медленнее чем через itertools

"""
import sys

buttons = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


def listing(strng):
    # Превращаем каждое значение по нужному ключу в список и создаем вложенный список с овсеми нужными элементами
    return [list(buttons[i]) for i in list(strng)]


def reverse_func(lst):
    try:
        # комбинируем два первых элемента (два списка) списка, получая пары
        new_combination = [i + j for j in lst[1] for i in lst[0]]
        # удаляем два старых элемента и заменяем новым скомбинированым списком
        del lst[0:2]
        lst.insert(0, new_combination)
        # возвращаем на вход функции новый список, где повторяется комбинирование по парам уже с новыми данными
        return reverse_func(lst)
    except IndexError:
        return lst
        # используем try/except для нахождения конца опираций, можно заменить на проверку длины списка
        # (пока не будет равна 1)



def main(argv):
    return reverse_func(listing(argv[0]))


if __name__ == "__main__":
    print(main(sys.argv[1:]))
