import sys
import time

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[-1]
    L = []
    E = []
    G = []
    for i in arr:
        if i < pivot:
            L.append(i)
        elif i == pivot:
            E.append(i)
        else:
            G.append(i)
    sorted_L = quick_sort(L)
    sorted_G = quick_sort(G)
    return sorted_L+E+sorted_G
    

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0].strip())
    numbers = list(map(int, lines[1].split()))
    print("Input numbers:", numbers)
    algs = [("Insertion sort", insertion_sort),
            ("Merge sort", merge_sort),("Quick sort", quick_sort)]
    for name, sort_func in algs:
        start_time = time.time()
        sorted_arr = sort_func(numbers)
        end_time = time.time()
        print(f"\n{name}result: {sorted_arr}")
        print(f"Running time: {end_time - start_time:.6f}seconds")
        print(f"Check: {sorted_arr == sorted(numbers)}")

if __name__ == "__main__":
    main()
