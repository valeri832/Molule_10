import os
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]

    for filename in filenames:
        if not os.path.exists(filename):
            print(f"Файл {filename} НЕ найден!")
            exit(1)

    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f"Линейное выполнение: {linear_time:.6f} секунд")

    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    parallel_time = time.time() - start_time
    print(f"Многопроцессорное выполнение: {parallel_time:.6f} секунд")
    
