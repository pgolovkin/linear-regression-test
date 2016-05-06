import random
import sys
import os


#считаем сумму разниц реального и рассчитанного результата * на значение переменной
def calcSum(index):
    sum = 0
    for i in range(0, len(x)):
        sum += (t0 + t1 * x[i][0] + t2 * x[i][1] + t3 * x[i][2] - y[i]) * (x[i][index] if index >= 0 else 1)
    return sum

#считаем среднее квадратичное отклонение от реального результата
def calcDifference():
    sum = 0
    for i in (0, len(x) - 1):
        sum += (t0 + t1 * x[i][0] + t2 * x[i][1] + t3 * x[i][2] - y[i]) ** 2
    return sum / (2 * m)

#исходные данные
# |1|2|3    |6
# |4|5|6    |9
# |7|8|9    |12
x = [[1,2,3], [2,3,4], [3,4,5]]
y = [6, 9, 12]

#начальные значения переменных
t0 = 0;
t1 = 0;
t2 = 0;
t3 = 0;

#скорость обучения
alfa = 0.0001
m = len(x)

#точность обучения
epsilon = 0.0001
while (calcDifference() > epsilon):
    _t0 = t0 - alfa * (1 / m) * calcSum(-1)
    _t1 = t1 - alfa * (1 / m) * calcSum(0)
    _t2 = t2 - alfa * (1 / m) * calcSum(1)
    _t3 = t3 - alfa * (1 / m) * calcSum(2)
    t0 = _t0
    t1 = _t1
    t2 = _t2
    t3 = _t3

print(t0, ' + x1 * ',t1,' + x2 * ',t2,' + x3 * ',t3)

for i in range(0,3):
    _y = t0 + x[i][0] * t1 + x[i][1] * t2 + x[i][2] * t3
    print (_y, ' and real is ', y[i])





