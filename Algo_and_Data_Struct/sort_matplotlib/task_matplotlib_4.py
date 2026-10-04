import matplotlib.pyplot as plt
import numpy as np

# Построить на одном графике функции синуса и косинуса
# Использовать разные цвета и стили линий


def plt_several_graphs() -> None:
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    fig, ax = plt.subplots()

    ax.plot(x, y_sin, color='brown', linestyle='--', label='$sin(x)$')
    ax.plot(x, y_cos, color='green', label='$cos(x)$')

    ax.set_title('Построение нескольких графиков')
    ax.set_xlabel('Ось x')
    ax.set_ylabel('Ось y')

    ax.grid(True, linestyle=':', alpha=0.6)

    ax.legend()

    fig.savefig('intersecting_graphs.png', dpi=300, bbox_inches='tight')

    plt.show()


def matplotlib_manipulation() -> None:
    plt_several_graphs()


if __name__ == '__main__':
    matplotlib_manipulation()
