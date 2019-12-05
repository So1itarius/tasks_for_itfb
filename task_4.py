"""
4. Реализовать алгоритм. Дана строка A, которая представляет из себя камни, являющиеся алмазами,
 и строка K, в которой камни.
Каждый символ из строки К - это камень. Задача: найти все  камни в строке К, которые одновременно
являются и алмазами и камнями. Символы в строке А не повторяются. Алфавит строк А и К = {от А до я}.
Символы в строке
чувствительны к регистру (камень "А" != камню "а")
Пример 1: Вход: А = "aA", К = "аAAбббб"
Вывод: 3
Пример 2: Ввод: А = "я", К = "ЯЯ"
Вывод: 0
Примечание :
• А и К - строки, длина которых не более 50 символов.
• Символы в А не повторяются.
 """
import re
import sys


def main(argv):
    # с помощью рег. выражений ищем и считаем совпадения
    result = re.findall(f"{list(argv[0])}", argv[1])
    print("Вывод для способа 1:", len(result))

    # перебираем влоб циклом, сравнивая каждое с каждым
    sum = 0
    for i in argv[0]:
        for j in argv[1]:
            if i == j:
                sum += 1
    print("Вывод для способа 2:", sum)


if __name__ == "__main__":
    main(sys.argv[1:])