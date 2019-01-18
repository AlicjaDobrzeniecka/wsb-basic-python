
# Write a program which plots function f(x) = x/(-3) + a for x <= 0 f(x) = x*x/3 dla x >= 0
# and based on user input with x in range <-10,10>

import matplotlib.pyplot as plt
import numpy as np


def plot():

    a = float(input('Enter a: '))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x_1 = np.linspace(-10, 0)
    y_1 = x_1 / (-3) + a

    x_2 = np.linspace(0, 10)
    y_2 = x_2 * x_2 / 3

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    plt.plot(x_2, y_2, '--', label='x * x / 3')
    plt.plot(x_1, y_1, '--', label='x / (-3) + a')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('Plot of functions')
    plt.legend(loc='upper left')
    plt.show()


plot()
