import matplotlib.pyplot as plt
import numpy as np

# Создать гистограмму распределения оценок студентов
# (данные: 4, 5, 3, 4, 5, 5, 4, 3, 2, 4)


def plt_ax_hist(data: list = None) -> None:
    frequencies = {x : data.count(x) for x in data}
    fig, ax = plt.subplots()
    ax.bar(frequencies.keys(), frequencies.values(), color='m')
    ax.set_title('Распределение оценок студентов')
    ax.set_xlabel('Оценки')
    ax.set_ylabel('Количество студентов')
    ax.set_xticks(np.arange(1, max(data) + 1, 1))
    ax.set_yticks(np.arange(0, max(frequencies.values()) + 1, 1))
    ax.grid(axis='y')

    fig.savefig('student_marks_histogram.png', dpi=300, bbox_inches='tight')

    plt.show()


def matplotlib_manipulation() -> None:
    task_1_data = [4, 5, 3, 4, 5, 5, 4, 3, 2, 4]
    plt_ax_hist(task_1_data)


if __name__ == '__main__':
    matplotlib_manipulation()
