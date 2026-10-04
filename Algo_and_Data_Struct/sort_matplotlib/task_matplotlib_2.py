import matplotlib.pyplot as plt
import numpy as np

# Построить график функции  y=x2  на отрезке [-10, 10]
# Добавить заголовок графика
# Подписать оси координат


def plt_graph(left_bound: float, right_bound: float) -> None:
    x = np.linspace(left_bound, right_bound, 100)
    y = np.square(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, color='red', label='$y=x^2$')
    ax.set_title('График функции $y=x^2$ на отрезке [-10, 10]')
    ax.set_xlabel('Ось x')
    ax.set_ylabel('Ось y')

    ax.grid(True, linestyle=':', alpha=0.6)

    ax.legend()

    fig.savefig('square_function_graph.png', dpi=300, bbox_inches='tight')

    plt.show()


def matplotlib_manipulation() -> None:
    task_2_data = (-10, 10)
    plt_graph(*task_2_data)


if __name__ == '__main__':
    matplotlib_manipulation()
