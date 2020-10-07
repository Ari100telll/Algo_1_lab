from manager.farm_utils import *


if __name__ == '__main__':
    farms = get_farm_arr_from_file("data/input_farm_data.csv")
    print_farm_array(farms)

    print("=============================================")

    sort_farm_fan_power_wt_descending(farms)
    print_farm_array(farms)

    print("=============================================")

    sort_farm_count_of_animals_ascending(farms)
    print_farm_array(farms)
