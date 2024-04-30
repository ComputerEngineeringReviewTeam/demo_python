linear_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

def multiply5(x):
    return 5*x

#TODO: Wykorzystaj Process Pool, w celu zrownoleglenia obliczen (w tym przypadku jest to mnozenie wektora przez skalar). Przyklad uzycia modulu 'multiprocessing' w pliku example.py
linear_matrix = map(multiply5, linear_matrix)

print(list(linear_matrix))

    