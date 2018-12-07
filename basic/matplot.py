import matplotlib.pyplot as plt
import numpy as np


def draw_by_xy():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([3, 5, 7, 6, 2, 6, 10, 15])
    plt.plot(x, y, 'r')  # 折线 1 x 2 y 3 color
    plt.plot(x, y, 'g', lw=10)  # 4 line w
    # 折线 饼状 柱状
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([13, 25, 17, 36, 21, 16, 10, 15])
    plt.bar(x, y, 0.2, alpha=1, color='b')  # 5 color 4 透明度 3 0.9
    plt.show()


def draw_by_func():
    x = np.linspace(0, 1, 200)
    plt.plot(x, x, label='x')
    plt.plot(x, x ** 2, label='x^2')
    plt.plot(x, x ** 3, label='x^3')
    plt.plot(x, x ** 4, label='x^4')
    plt.plot(x, x ** 5, label='x^5')
    # plt.plot(x, np.exp(x), label='e^x')
    plt.plot(x, x ** 0.5, label='x^0.5')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title('simple plot')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    draw_by_xy()
    draw_by_func()
