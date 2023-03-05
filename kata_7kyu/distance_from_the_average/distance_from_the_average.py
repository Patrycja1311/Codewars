import numpy as np


def distances_from_average(test_list):
    mean_list = np.mean(test_list)
    results = [round(mean_list - i, 2) for i in test_list]
    return print(results)


if __name__ == '__main__':
    distances_from_average([55, 95, 62, 36, 48])
    distances_from_average([1, 1, 1, 1, 1])
    distances_from_average([2, -2])