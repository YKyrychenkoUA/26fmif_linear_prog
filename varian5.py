"""
Задача №5:
Мінімізувати вартість суміші:
Z = 3*x1 + 2*x2 -> min
Використовуємо lingprog тому множим на -1
Z = -3*x1 - 2*x2 -> max

Обмеження (мінімальний вміст добавок):
4*x1 + 5*x2 >= 40   (X)
2*x1 + 1*x2 >= 14   (Y)
3*x1 + 1*x2 >= 18   (Z)
x1 >= 0, x2 >= 0

Використовуємо lingprog тому множим на -1-4*x1 - 5*x2 <= -40
-2*x1 - 1*x2 <= -14
-3*x1 - 1*x2 <= -18
"""

from scipy.optimize import linprog

cost_coefficients = [3, 2]

A_ub = [
    [-4, -5],
    [-2, -1],
    [-3, -1]
]

b_ub = [-40, -14, -18]

x1_bounds = (0, None)
x2_bounds = (0, None)

# Розв'язуємо задачу лінійного програмування
result = linprog(cost_coefficients, A_ub=A_ub, b_ub=b_ub, bounds=[x1_bounds, x2_bounds], method='highs')

print(result.fun)
print(f"x1 (компанія A) = {result.x[0]}")
print(f"x2 (компанія B) = {result.x[1]}")
