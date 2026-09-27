def sum_interval(a, b):
    start = min(a, b)
    end = max(a, b)
    count = end - start + 1
    return (start + end) * count // 2

if __name__ == "__main__":
    print("Результат работы sum_interval.py:")
    print(sum_interval(1, 5))  # Должно вывести 15 (1+2+3+4+5)
