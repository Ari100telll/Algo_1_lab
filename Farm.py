from typing import List


class Farm:

    def __init__(self, place: str, count_of_animals: int, fan_power_wt: float):
        self.place = place
        self.count_of_animals = count_of_animals
        self.fan_power_wt = fan_power_wt

    def __str__(self):
        return self.place + " " + str(self.count_of_animals) + " " + str(self.fan_power_wt)


def sort_farm_fan_power_wt_descending(farm_arr: List[Farm]):
    for i_iterator in range(len(farm_arr) - 1, 0, -1):
        for j_iterator in range(i_iterator):
            if farm_arr[j_iterator].fan_power_wt < farm_arr[j_iterator + 1].fan_power_wt:
                farm_arr[j_iterator], farm_arr[j_iterator + 1] = farm_arr[j_iterator + 1], farm_arr[j_iterator]


def sort_farm_count_of_animals_ascending(farm_arr: List[Farm]):

    farm_arr_size = len(farm_arr)

    def heapify(farms_array, size, i_index):

        largest_index = i_index
        l_index = i_index * 2 + 1
        r_index = i_index * 2 + 2

        if l_index < size and farms_array[largest_index].count_of_animals < farms_array[l_index].count_of_animals:
            largest_index = l_index

        if r_index < size and farms_array[largest_index].count_of_animals < farms_array[r_index].count_of_animals:
            largest_index = r_index

        if largest_index != i_index:
            farms_array[i_index], farms_array[largest_index] = farms_array[largest_index], farms_array[i_index]
            heapify(farms_array, size, largest_index)

    for i_iterator in range(farm_arr_size, -1, -1):
        heapify(farm_arr, farm_arr_size, i_iterator)

    for i_iterator in range(farm_arr_size - 1, 0, -1):
        farm_arr[i_iterator], farm_arr[0] = farm_arr[0], farm_arr[i_iterator]  # свап
        heapify(farm_arr, i_iterator, 0)


if __name__ == '__main__':
    farms = [Farm("California", 17, 200), Farm("California1", 3, 400), Farm("California2", 7, 550),
             Farm("California3", 6, 28), Farm("California4", 15, 346)]
    sort_farm_fan_power_wt_descending(farms)
    for farm in farms:
        print(farm)
    print("--------------------------")
    sort_farm_count_of_animals_ascending(farms)
    for farm in farms:
        print(farm)
