import numpy as np
import math

def length_of_curve(f, a, b):
    n = 1000

    delta_x = (b - a) / n

    sum_of_lengths = 0
    for i in range(n):
        x_i = a + i * delta_x
        x_i_plus_1 = a + (i + 1) * delta_x

        if x_i <= 0 or x_i_plus_1 <= 0:
            continue

        y_i = f(x_i)
        y_i_plus_1 = f(x_i_plus_1)

        length_of_line_segment = math.sqrt((x_i_plus_1 - x_i)**2 + (y_i_plus_1 - y_i)**2)
        sum_of_lengths += length_of_line_segment

    return sum_of_lengths

def f(x):
    return x**2 - (np.lib.scimath.log(x)/8)

length_of_curve_result = length_of_curve(f, 1, 3)

print(length_of_curve_result)

#RESULTADO É 8.14