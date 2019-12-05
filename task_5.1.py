"""
Решение влоб, через рекурсивную функцию

"""
import sys

buttons = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


def listing(strng):
    return [list(buttons[i]) for i in list(strng)]


def reverse_func(lst):
    try:
        c = [i + j for j in lst[1] for i in lst[0]]
        lst.remove(lst[0])
        lst.remove(lst[0])
        lst.insert(0, c)
        return reverse_func(lst)
    except:
        return lst


def main(argv):
    return reverse_func(listing(argv[0]))


if __name__ == "__main__":
    print(main(sys.argv[1:]))
