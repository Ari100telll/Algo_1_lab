from model.algo_statistics import AlgoStatistics
from typing import List
from model.farm import Farm


def sort_farm_fan_power_wt_descending(farm_arr: List[Farm]):
    Statistics = AlgoStatistics("Bubble sort")
    for i_iterator in range(len(farm_arr) - 1, 0, -1):
        for j_iterator in range(i_iterator):
            Statistics.add_compares()
            if farm_arr[j_iterator].fan_power_wt < farm_arr[j_iterator + 1].fan_power_wt:
                Statistics.add_swaps()
                farm_arr[j_iterator], farm_arr[j_iterator + 1] = farm_arr[j_iterator + 1], farm_arr[j_iterator]
    Statistics.print_statistics()


def sort_farm_count_of_animals_ascending(farm_arr: List[Farm]):
    Statistics = AlgoStatistics("Heapsort")

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
