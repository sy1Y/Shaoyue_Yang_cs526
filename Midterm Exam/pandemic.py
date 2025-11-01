import sys

def main():
    lines = sys.stdin.read().strip().splitlines()
    matrix_num = int(lines[0])
    #infected counties location
    infect_counties = set()
    for i in range(1,len(lines)):
        x, y = map(int, lines[i].split())
        infect_counties.add((x, y))
            
    def is_neibour(x,y):
        #Define the range of adjacent coordinates
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x2, y2 = x + dx, y + dy
            #Boundary checks
            if 0<=x2<matrix_num and 0<=y2<matrix_num:
                yield(x2,y2) #Return the coordinates of neighbor one-by-one 
    day = 0
    #check neighbour countries of infected countries
    while True:
        new_infect = set()
        for x in range(matrix_num):
            for y in range(matrix_num):
                if (x,y) not in infect_counties:
                    #count the numbers of infected neighbors
                    count = sum((x2,y2) in infect_counties for x2,y2 in is_neibour(x,y))
                    if count >= 2:
                        new_infect.add((x,y))
        #If there are no new infections, stop infection
        if not new_infect:
            break
        #Otherwise,updated new infected counties
        day += 1
        infect_counties |= new_infect
    #calculate and print the result
    total = matrix_num * matrix_num
    healthy = total - len(infect_counties)
    if healthy == 0:
        print("There are no healthy counties left")
    else:
        print("There are healthy counties left")
                        
#Program Entry
if __name__ == "__main__":
    main()
        
    
