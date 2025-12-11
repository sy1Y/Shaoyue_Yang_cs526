import sys

def longest_path(matrix, row, col):
    #Record the length of the longest descending path starting from (x, y)
    memo = [[None]*col for each in range(row)]
    directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    def dfs(x,y):
        if memo[x][y] is not None:
            return memo[x][y]
        max_len = 0
        #Iterate through the 8-neighboring
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < row and 0 <= ny < col: #Boundary check
                if matrix[nx][ny] < matrix[x][y]: #Descending check 
                    max_len = max(max_len, dfs(nx,ny)+1)
        memo[x][y] = max_len
        return max_len

    #Finding the globally longest decreasing path
    longest = 0
    for i in range(row):
        for j in range(col):
            longest = max(longest, dfs(i,j))
    return longest

def main():
    lines = sys.stdin.read().strip().splitlines()
    row = int(lines[0])
    col = int(lines[1])
    matrix = []
    for i in range(row):
        matrix.append(list(map(int, lines[2+i].split())))
    result = longest_path(matrix, row, col)
    print(result)

if __name__ == "__main__":
    main()
