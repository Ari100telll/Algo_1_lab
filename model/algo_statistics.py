import time


class AlgoStatistics:
    def __init__(self, Algo_name):
        self.name = Algo_name
        self.start_time = time.time()
        self.compares = 0
        self.swaps = 0

    def get_work_time(self):
        work_time = time.time() - self.start_time
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