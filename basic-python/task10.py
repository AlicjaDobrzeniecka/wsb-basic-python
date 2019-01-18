
# Three different plots

import matplotlib.pyplot as plt
import numpy as np


def plot():

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x_1= np.linspace(-10, 10)
    y_1 = x_1
    x_2 = np.linspace(-10, 10)
    y_2 = x_2 * x_2
    x_3 = np.linspace(-10, 10)
    y_3 = 2 * x_3 + 1

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    plt.plot(x_1, y_1, ':', label='x')
    plt.plot(x_2, y_2, '-', label='x * x')
    plt.plot(x_3, y_3, '--', label='ax + b')
    plt.legend(loc='upper left')
    plt.show()


plot()


