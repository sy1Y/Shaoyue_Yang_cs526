import sys
import time

def radix_sort(arr):
    a = arr.copy()
    max_num = max(arr)
    exp = 1
    while max_num//exp > 0:
        buckets = [[] for _ in range(10)]
        for num in a:
            digit = (num//exp) % 10
            buckets[digit].append(num)
        a = []
        for bucket in buckets:
            a.extend(bucket)
        exp *= 10
    return a

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0].strip())
    numbers = list(map(int, lines[1].split()))
    print("Input numbers:", numbers)
    start_time = time.time()
    sorted_arr = radix_sort(numbers)
    end_time = time.time()
    print(f"\nradix sort result: {sorted_arr}")
    print(f"Running time: {end_time - start_time:.6f}seconds")
    print(f"Check: {sorted_arr == sorted(numbers)}")

if __name__ == "__main__":
    main()
