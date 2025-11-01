import sys

def main():
    lines = sys.stdin.read().strip().splitlines()
    day = int(lines[0])
    total_snow = list(map(int,lines[1].split()))
    total_snow.insert(0,0) #snowfall start at 0

    sum_snow = total_snow[-1]
    half = sum_snow/2

    def check_threeDay(total_snow):
        for i in range(len(total_snow)-3):
            total_threeDay = total_snow[i+3] - total_snow[i]
            if total_threeDay > half:
                return "Yes"
        return "No"
    print("Number of days:", day)
    print(lines[-1])
    print("solution:",check_threeDay(total_snow))

if __name__ == "__main__":
    main()
