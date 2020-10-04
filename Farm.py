from typing import List
import time


class Algo_statistics:
    def __init__(self, Algo_name):
        self.name = Algo_name
        self.start_time = time.time()
        self.compares = 0
        self.swaps = 0

    def get_work_time(self):
        work_time = self.start_time - time.time()
        return work_time

    def add_compares(self):
        self.compares += 1

    def add_swaps(self):
        self.swaps += 1

    def print_statistics(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print(self.name)
        print(f"Work_time: {self.get_work_time()}")
        print(f"Compares: {self.compares}")
        print(f"Swaps: {self.swaps}")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")


class Farm:
    def __init__(self, place: str, count_of_animals: int, fan_power_wt: float):
        self.place = place
        self.count_of_animals = count_of_animals
        self.fan_power_wt = fan_power_wt

    def __str__(self):
        return self.place + " " + str(self.count_of_animals) + " " + str(self.fan_power_wt)


def sort_farm_fan_power_wt_descending(farm_arr: List[Farm]):
    Statistics = Algo_statistics("Bubble sort")
    for i_iterator in range(len(farm_arr) - 1, 0, -1):
        for j_iterator in range(i_iterator):
            Statistics.add_compares()
            if farm_arr[j_iterator].fan_power_wt < farm_arr[j_iterator + 1].fan_power_wt:
                Statistics.add_swaps()
                farm_arr[j_iterator], farm_arr[j_iterator + 1] = farm_arr[j_iterator + 1], farm_arr[j_iterator]
    Statistics.print_statistics()


def sort_farm_count_of_animals_ascending(farm_arr: List[Farm]):
    Statistics = Algo_statistics("Heapsort")

    farm_arr_size = len(farm_arr)

    def heapify(farms_array, size, i_index):

        largest_index = i_index
        l_index = i_index * 2 + 1
        r_index = i_index * 2 + 2

        Statistics.add_compares()
        if l_index < size and farms_array[largest_index].count_of_animals < farms_array[l_index].count_of_animals:
            largest_index = l_index

        Statistics.add_compares()
        if r_index < size and farms_array[largest_index].count_of_animals < farms_array[r_index].count_of_animals:
            largest_index = r_index

        Statistics.add_compares()
        if largest_index != i_index:
            Statistics.add_swaps()
            farms_array[i_index], farms_array[largest_index] = farms_array[largest_index], farms_array[i_index]
            heapify(farms_array, size, largest_index)

    for i_iterator in range(farm_arr_size, -1, -1):
        heapify(farm_arr, farm_arr_size, i_iterator)

    for i_iterator in range(farm_arr_size - 1, 0, -1):
        Statistics.add_swaps()
        farm_arr[i_iterator], farm_arr[0] = farm_arr[0], farm_arr[i_iterator]  # свап
        heapify(farm_arr, i_iterator, 0)
    Statistics.print_statistics()


def get_farm_arr_from_file(File_Name):
    farm_arr = []
    with open(File_Name, 'r', encoding='utf-8') as file:
        i = 0
        for line in file:
            line = line.strip()
            arr = line.split(',')
            place = arr[0]
            count_of_animals = int(arr[1])
            fan_power_wt = float(arr[2])
            farm_arr.append(Farm(place, count_of_animals, fan_power_wt))
    return farm_arr
    pass


def print_farm_array(farm_arr: List[Farm]):
    for farm_element in farm_arr:
        print(farm_element)


if __name__ == '__main__':
    farms = get_farm_arr_from_file("input_data.csv")
    print_farm_array(farms)

    print("=============================================")

    sort_farm_fan_power_wt_descending(farms)
    print_farm_array(farms)

    print("=============================================")

    sort_farm_count_of_animals_ascending(farms)
    print_farm_array(farms)
