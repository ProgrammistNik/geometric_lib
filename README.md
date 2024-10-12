# Introduction
Калькулятор предназначен для быстрого вычисления площади и периметра различных фигур, вводя нужные параметры через командную строку.

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# General description
Можно вычислить площадт или периметр круга, треугольника, квадрата и прямоугольника

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Функции

### Circle
**area(r)**: Считает площадь круга с заданным радиусом 'r'
Например 'area(2)' вернет '12,57'

**perimeter(r)**: Считает длину окружности с заданным радиусом `r`
Например `perimeter(2)` вернёт `6,28`

### Square
**area(a)**: Считает площадь квадрата с заданной стороной `a`
Например `area(2)` вернёт `4`

**perimeter(a)**: Считает периметр квадрата с заданной `a`
Например `perimeter(2)` вернёт `8`

### Triangle
**area(a, b, c)**: Считает площадь треугольника с заданными сторонами 'a', 'b' и 'c'
Например `area(5, 12, 13)` вернёт `30`

**perimeter(a, b, c)**: Считает периметр треугольника с задаными сторонами 'a', 'b' и 'с'
Например `perimeter(5, 12, 13)` вернёт `30`

# Commit history
Commit 'e56938a206bd0faa548930ea5c84' (added documentation)
