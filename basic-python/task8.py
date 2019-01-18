
# Write a program which plots function y = ax + b based on user input with x in range <-10,10>
# Add info on plot whether the function increases or decreases with time

import matplotlib.pyplot as plt
import numpy as np


def plot():

    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x_vals = np.linspace(-10, 10)
    y_vals = a + b * x_vals

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    if b <0:
        t = 'The function is decreasing'
    elif b >=0:
        t = "The function is increasing"

    plt.plot(x_vals, y_vals, '--', label=t)
    plt.legend(loc='upper left')
    plt.show()


plot()
