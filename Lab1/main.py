import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    coef = 0
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        coef = int(coef_str)
    except:
        # Вводим с клавиатуры
        print(prompt)
        while True:
            coef_str = input()
            try:
                coef = float(coef_str)
            except ValueError:
                print('Введено некорректное значение')
                print(prompt)
                continue
            else:
                break
    # Переводим строку в действительное число

    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D1 = b * b - 4 * a * c
    if D1 == 0.0:
        pseudo_root = -b / (2.0 * a)
        if pseudo_root >= 0:
            root = math.sqrt(pseudo_root)
            result.append(root)
            result.append(-root)
    elif D1 > 0.0:
        sqD1 = math.sqrt(D1)
        pseudo_root1 = (-b + sqD1) / (2.0 * a)
        pseudo_root2 = (-b - sqD1) / (2.0 * a)
        if pseudo_root1 > 0:
            root = math.sqrt(pseudo_root1)
            result.append(root)
            result.append(-root)
        elif pseudo_root1 == 0:
            result.append(pseudo_root1)
        if pseudo_root2 >= 0:
            root = math.sqrt(pseudo_root2)
            result.append(root)
            result.append(-root)
        elif pseudo_root2 == 0:
            result.append(pseudo_root2)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4