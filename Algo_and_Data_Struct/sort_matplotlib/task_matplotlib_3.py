import matplotlib.pyplot as plt

# Построить круговую диаграмму распределения продаж по категориям товаров
# Добавить процентные значения

def plt_round_diagram(data: dict) -> None:
    fig, ax = plt.subplots()
    ax.pie(data.values(), labels=data.keys(), autopct='%1.2f%%', startangle=90)

    ax.set_title('Продажи наушников по типам и аксессуаров')

    fig.savefig('sales_round_diagram.png', dpi=300, bbox_inches='tight')

    plt.show()


def matplotlib_manipulation() -> None:
    task_3_data = {
        "Внутриканальные": 12,
        "Вставные": 21,
        "Накладные": 15,
        "Мониторные": 5,
        "Аксессуары": 7
    }
    plt_round_diagram(task_3_data)


if __name__ == '__main__':
    matplotlib_manipulation()
