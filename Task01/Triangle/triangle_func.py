class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(side1, side2, side3):
    """
    Функция определяет тип треугольника по длинам его сторон.

    Аргументы:
    side1 (float): Длина первой стороны треугольника.
    side2 (float): Длина второй стороны треугольника.
    side3 (float): Длина третьей стороны треугольника.

    Возвращает:
    str: Тип треугольника: "nonequilateral" (разносторонний), "isosceles" (равнобедренный), "equilateral" (равносторонний).

    Примеры:
    >>> get_triangle_type(5, 5, 5)
    'equilateral'

    >>> get_triangle_type(4, 4, 6)
    'isosceles'

    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'

    >>> get_triangle_type(-2, 3, 4)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Incorrect side lengths of a triangle

    >>> get_triangle_type(1, 1, 10)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Incorrect side lengths of a triangle

    >>> get_triangle_type(0, 4, 5)
    Traceback (most recent call last):
    ...
    IncorrectTriangleSides: Incorrect side lengths of a triangle
    """
    if side1 <= 0 or side2 <= 0 or side3 <= 0 or side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise IncorrectTriangleSides("Incorrect side lengths of a triangle")

    if side1 == side2 == side3:
        return "equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "isosceles"
    else:
        return "nonequilateral"

if __name__ == "__main__":
    import doctest
    doctest.testmod()