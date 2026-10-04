# Task 1 functions
def merge_desc(left: list = None, right: list = None) -> list:
    """Merge two sorted lists with two pointers method and descending order"""
    sorted_list_desc = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_list_desc.append(left[i])
            i += 1
        else:
            sorted_list_desc.append(right[j])
            j += 1

    sorted_list_desc.extend(left[i:])
    sorted_list_desc.extend(right[j:])

    return sorted_list_desc


def merge_sorted_desc(arr: list | None = None) -> list | None:
    """Sort incoming list (merge sort) with descending order.

    :param arr: list
    :return:
    """
    if arr is None:
        return None

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sorted_desc(arr[:mid])
    right = merge_sorted_desc(arr[mid:])

    return merge_desc(left, right)
# Task 1 end


# Task 2
def sort_len_str(arr: list = None) -> None:
    """Sort a list of str by length (inplace)"""
    if arr is None or len(arr) <= 1:
        return arr

    arr.sort(key=len)


# Task 3
def sort_by_digits_sum(arr: list = None) -> None:
    """Sort a list of integers by digits sum"""
    if arr is None or len(arr) <= 1:
        return arr

    arr.sort(key=lambda n: (sum(map(int, str(n))), n))
    # Второй аргумент n нужен для сортировки по возрастанию при одинаковой сумме цифр


# Task 4
def sorted_by_frequency(arr: list = None) -> list | None:
    """Deduplicate a list of str and sort it by frequency in the incoming list"""
    if arr is None or len(arr) <= 1:
        return arr

    rle = dict()
    for s in arr:
        rle[s] = rle.get(s, 0) + 1

    result = sorted(rle.keys(), key=lambda s: (rle[s], s), reverse=True)
    return result


def template_sort_task_output(task_number: int, task_desc: str, sort_list: list, function,
                              inplace: bool = True) -> None:
    """Prints formatted output for each task.

    :param task_number: Task number
    :param task_desc: Task description
    :param sort_list: List for sorting
    :param function: Sort function
    :param inplace: Specifies if the sorting is inplace or returns a new collection
    :return:
    """
    print(f'Задание {task_number}: {task_desc}')
    print(f'Входные данные: {sort_list}')
    if inplace:
        function(sort_list)
        result = sort_list
    else:
        result = function(sort_list)
    print(f'Результат: {result}')


def sort_output() -> None:
    """Organizes sort tasks execution and output"""
    print('Блок Sort')
    task_1_desc = 'отсортировать список чисел в порядке убывания, не используя встроенные методы сортировки.'
    task_1_sort_list = [5, 2, 9, 1, 5]
    template_sort_task_output(1, task_1_desc, task_1_sort_list, merge_sorted_desc, inplace=False)

    task_2_desc = 'отсортировать список строк по их длине в порядке возрастания.'
    task_2_sort_list = ["apple", "banana", "kiwi", "pear"]
    template_sort_task_output(2, task_2_desc, task_2_sort_list, sort_len_str, inplace=True)

    task_3_desc = 'отсортировать список чисел по сумме их цифр.'
    task_3_sort_list = [123, 45, 6, 789]
    template_sort_task_output(3, task_3_desc, task_3_sort_list, sort_by_digits_sum, inplace=True)

    task_4_desc = 'отсортировать список слов по частоте их встречаемости в тексте.'
    task_4_sort_list = ["apple", "banana", "apple", "cherry", "banana"]
    template_sort_task_output(4, task_4_desc, task_4_sort_list, sorted_by_frequency, inplace=False)


if __name__ == '__main__':
    sort_output()
