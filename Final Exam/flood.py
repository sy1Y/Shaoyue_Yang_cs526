import sys
import heapq

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    threshold = int(lines[1])
    drain = int(lines[2])
    cracks = []
    idx = 3 #crack begining position
    for i in range(n):
        #time of crack appearance,initial crack size
        t, s = map(int, lines[3 + i].split())
        cracks.append((t,s))
        idx += 2
    heap = [] #max heap for crack size
    floodwater = 0
    max_flood = 0
    time = 0
    ptr = 0 # pointer to crack list
    
    #iterate until all cracks handled & heap empty
    while ptr<n or heap:
        #add all cracks appearing at this time
        while ptr<n and cracks[ptr][0] == time:
            t, size = cracks[ptr]
            heapq.heappush(heap, -size)
            ptr += 1
        if heap: #repair exactly one crack
            heapq.heappop(heap)
            
        total_leak = -sum(heap) #compute water in this time unit
        floodwater += total_leak
        floodwater -= drain
        if floodwater < 0:
            floodwater = 0
        if floodwater >= threshold:
            print("FLOOD")
            print(time)
            print(floodwater)
            return
        max_flood = max(max_flood, floodwater)
        
        #increase all remaining cracks by 1
        if heap:
            heap = [h-1 for h in heap]
            heapq.heapify(heap)
        time+= 1

    #no flood
    print("SAFE")
    print(max_flood)
        
if __name__ == "__main__":
    main()
