import time
import tracemalloc


def create_file():
    with open("10_million_lines.txt", "w") as f:
        for i in range(1, 10_000_001):
            f.write(f"This is line number {i}\n")


def Lines_to_List():
    with open("10_million_lines.txt", "r") as file:
        lines = []
        for line in file:
            lines.append(line)
    return lines


def yield_line():
    with open("10_million_lines.txt", "r") as file:
        for line in file:
            yield line


def main():
    # create_file()
    with open("10_million_lines.txt", "r") as f:

        tracemalloc.start()
        start = time.perf_counter()

        for i in f:
            pass

        end = time.perf_counter()
        mem1 = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"List time:{end-start:.6f}")
        print("List memory:", mem1[1] / 1024 / 1024, "MB")

        tracemalloc.start()
        start = time.perf_counter()

        for i in yield_line():
            pass

        end = time.perf_counter()
        mem2 = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"yield time:{end-start:.6f}")
        print("yield memory:", mem2[1] / 1024 / 1024, "MB")


main()
