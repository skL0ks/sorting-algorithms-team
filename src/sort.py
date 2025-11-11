def bubble_sort(arr):
    """
    Сортировка пузырьком.
    Разработчик: Илья
    """
    n = len(arr)
    for i in range(n):
        # Флаг для оптимизации - если нет обменов, массив отсортирован
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если не было обменов, выходим досрочно
        if not swapped:
            break
    return arr


def quick_sort(arr):
    """
    Быстрая сортировка (Quick Sort).
    Разработчик: Антон
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """
    Сортировка слиянием (Merge Sort).
    Разработчик: Антон
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return _merge(left, right)


def _merge(left, right):
    """
    Вспомогательная функция для слияния двух отсортированных массивов.
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def benchmark_sorting(arr, algorithm):
    """
    Тестирование производительности алгоритма сортировки.
    Разработчик: Илья
    """
    import time
    start_time = time.time()
    result = algorithm(arr.copy())
    end_time = time.time()
    
    return {
        'algorithm': algorithm.__name__,
        'time': end_time - start_time,
        'sorted_array': result,
        'array_length': len(arr)
    }


# Пример использования
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    
    print("Исходный массив:", test_array)
    print("Bubble Sort:", bubble_sort(test_array.copy()))
    print("Quick Sort:", quick_sort(test_array.copy()))
    print("Merge Sort:", merge_sort(test_array.copy()))
    
    # Бенчмарк
    print("\nСравнение производительности:")
    algorithms = [bubble_sort, quick_sort, merge_sort]
    for algo in algorithms:
        result = benchmark_sorting(test_array, algo)
        print(f"{result['algorithm']}: {result['time']:.6f} сек")