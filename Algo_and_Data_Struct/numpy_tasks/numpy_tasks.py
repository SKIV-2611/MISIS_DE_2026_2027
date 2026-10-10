import numpy as np


def zeros_1d(task_num: int):
    z = np.zeros(10)
    print(f'{task_num}. вектор (одномерный массив) размера 10, заполненый нулями')
    print(f'{z=}')


def ones_1d(task_num: int):
    ones = np.ones(10, dtype='int32')
    print(f'{task_num}. вектор размера 10, заполненный единицами')
    print(ones)


def full_1d(task_num: int):
    full = np.full(10, fill_value=2.5)
    print(f'{task_num}. вектор размера 10, заполненный числом 2.5')
    print(full)


def ones_1d_zero_5(task_num: int):
    res1 = np.array((0, 0, 0, 0, 1, 0, 0, 0, 0, 0))
    res2 = np.zeros(10)
    res2[4] = 1
    res3 = np.eye(10)[4]
    print(f'{task_num}. вектор, заполненный нулями, но пятый элемент равен 1')
    print('созданный 3 разными способами:')
    print(f'{res1=}')
    print(f'{res2=}')
    print(f'{res3=}')


def vec_10_49(task_num: int):
    res = np.arange(10, 50, 1, dtype='int32')
    print(f'{task_num}. вектор со значениями от 10 до 49')
    print(res)


def reverse_array(task_num: int):
    a = np.arange(1, 11, 1, dtype='int32')
    a_flip = np.flip(a)
    print(f'{task_num}. Развернуть вектор (первый становится последним)')
    print(f'Initial array: {a=}')
    print(f'Array after np.flip(): {a_flip=}')
    a_rev = a[::-1]
    print(f'Array after reversing with slices: {a_rev=}')


def zero_to_eight_2d(task_num: int):
    res = np.arange(9).reshape((3, 3))
    print(f'{task_num}. Создать матрицу (двумерный массив) 3x3 со значениями от 0 до 8')
    print(f'Result:\n{res=}')


def find_non_zero_indices(task_num: int):
    a = np.array([1, 2, 0, 0, 4, 0])
    non_zero_indices = np.nonzero(a)
    print(f'{task_num}. Найти индексы ненулевых элементов в [1,2,0,0,4,0]')
    print(f'{non_zero_indices=}')


def random_3d(task_num: int):
    res = np.random.rand(3, 3, 3)
    print(f'{task_num}. Создать массив 3x3x3 со случайными значениями')
    print(f'Result:\n{res}')


def min_max_10_2d(task_num: int):
    a = np.random.randint(10_000, size=(10, 10))
    print(f'{task_num}. Создать массив 10x10 со случайными значениями, найти минимум и максимум')
    print(f'{a=}')
    min_a = np.min(a)
    max_a = np.max(a)
    print(f'Minimum value: {min_a}, Maximum value: {max_a}')


def ones_frame_2d(task_num: int):
    pre = np.ones((7, 7), dtype='int32')
    pre[1:-1, 1:-1] = 0
    print(f'{task_num}. Создать матрицу с 0 внутри и 1 на границах')
    print(f'{pre=}')


def chess_2d(task_num: int):
    chess = np.zeros((8, 8), dtype='int32')
    chess[0::2, 0::2] = 1
    chess[1::2, 1::2] = 1
    print(f'{task_num}. Создать матрицу 8x8 и заполнить ее в шахматном порядке')
    print(f'{chess=}')


def multiply_matrices_2d(task_num: int):
    a = np.random.randint(21, size=(5, 3))
    b = np.random.randint(16, size=(3, 2))
    c = np.matmul(a, b)
    print(f'{task_num}. Перемножить матрицы 5x3 и 3x2')
    print(f'{c=}')


def delete_columns_from_matrix_2d(task_num: int):
    a = np.random.randint(low=1, high=101, size=(5, 7))
    print(f'{task_num}. '
          f'Создать случайную матрицу 5x7 целых чисел от 1 до 100 '
          f'и удалить [3,5] колонки')
    print(f'{a=}')
    a_mod = np.delete(arr=a, obj=[2, 4], axis=1)
    print(f'{a_mod=}')


def make_array_from_generator(task_num: int):
    def generate():
        for x in range(10):
            yield x

    gen = generate()
    a = np.fromiter(gen, dtype='int32', count=-1)
    print(f'{task_num}. Есть генератор, сделать с его помощью массив')
    print(f'Result: {a=}')


def np_array_from_list_2d(task_num: int):
    li = [[1, 2, 3], [4, 5, 6]]
    res = np.array(li, dtype='int32')
    print('Доп.задание 1')
    print(f'{task_num}. Создать двумерный список'
          f' и преобразовать его в NumPy массив (с типом int32)')
    print(f'{res=}')


def are_2d_arrays_equal(task_num: int):
    a = np.zeros((4, 4), dtype='int32')
    b = np.zeros((4, 4), dtype='int32')
    print('Доп.задание 2')
    print(f'{task_num}. Проверить, одинаковы ли 2 NumPy массива')
    print(f'{a=}')
    print(f'{b=}')
    print(f'np.array_equal: {np.array_equal(a, b)}')
    print(f'(a == b).all(): {(a == b).all()}')
    fa = np.ones((3, 3), dtype='float64')
    fb = np.ones((3, 3), dtype='float64')
    print(f'{fa=}')
    print(f'{fb=}')
    print(f'np.array_equal(fa, fb): {np.array_equal(fa, fb)}')
    print(f'np.allclose(fa, fb): {np.allclose(fa, fb)}')


def make_array_frozen(task_num: int):
    a = np.arange(1, 11, 1)
    print('Доп.задание 3')
    print(f'{task_num}. Сделать массив неизменяемым')
    print(f'Array: {a=}')
    print(f'Is array mutable? {a.flags["WRITEABLE"]=}')
    a.flags['WRITEABLE'] = False
    print(f'Is array mutable? {a.flags["WRITEABLE"]=}')
    try:
        a[5] = 50
    except ValueError as e:
        print(f'Attempt to modify array: {e}')

    print(f'Array after modification attempt: {a=}')


if __name__ == '__main__':
    zeros_1d(1)
    print()
    ones_1d(2)
    print()
    full_1d(3)
    print()
    ones_1d_zero_5(4)
    print()
    vec_10_49(5)
    print()
    reverse_array(6)
    print()
    zero_to_eight_2d(7)
    print()
    find_non_zero_indices(8)
    print()
    random_3d(9)
    print()
    min_max_10_2d(10)
    print()
    ones_frame_2d(11)
    print()
    chess_2d(12)
    print()
    multiply_matrices_2d(13)
    print()
    delete_columns_from_matrix_2d(14)
    print()
    make_array_from_generator(15)
    print()

    # Additional
    np_array_from_list_2d(16)
    print()
    are_2d_arrays_equal(17)
    print()
    make_array_frozen(18)
