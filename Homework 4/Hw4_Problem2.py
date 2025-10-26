import sys

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0]) #Number of elements
    T = int(lines[1]) #Target value
    arr = list(map(int, lines[2].split())) #Array
    #Sorted numbers from the largest to smallest
    arr_sorted = sorted(arr, reverse=True)
    sum_num = 0
    count = 0
    for num in arr_sorted:
        sum_num += num
        count += 1
        if sum_num > T:
            break
    #Output the answer
    print(f"Answer: {count}")
# program entry point
if __name__ == "__main__":
    main()
