import sys

def get_longest(A, B):
    n = len(A)
    m = len(B)
    dpA = [1] * n #a list of length n and all elements are 1
    dpB = [1] * m
    #parentA[i] records the index of the previous element of A[i] in B
    parentA = [-1] * n 
    parentB = [-1] * m
    for i in range(n):
        for j in range(m):
            #if this condition is met,transfer from B[j] to A[i]
            if B[j] < A[i] and j<i:
                if dpA[i] < dpB[j]+1:
                    dpA[i] = dpB[j] + 1
                    parentA[i] = j
            #transfer from A[i] to B[j]
            if A[i] < B[j] and i<j:
                if dpB[j] < dpA[i] + 1:
                    dpB[j] = dpA[i] + 1
                    parentB[j] = i
    #Find the maximum length and the ending position
    max_len = 0
    last_index = -1
    is_in_A = False
    #Check the sequence that ends with an element in A
    for i in range(n):
        if dpA[i] > max_len:
            max_len = dpA[i]
            last_index = i
            is_in_A = True
    #Check the sequence that ends with an element in B
    for j in range(m):
        if dpB[j] > max_len:
            max_len = dpB[j]
            last_index = j
            is_in_A = False
    #Constructing a sequence by backtracking from the parent array
    result = []
    while last_index != -1:
        if is_in_A == True:
            result.append(A[last_index])
            last_index = parentA[last_index]
            is_in_A = False
        else:
            result.append(B[last_index])
            last_index = parentB[last_index]
            is_in_A = True
    result.reverse() # Reverse the sequence
    return max_len, result
    
def main():
    lines = sys.stdin.read().strip().splitlines()
    sizeA = int(lines[0].strip())
    sizeB = int(lines[1].strip())
    A = list(map(int, lines[2].strip().split()))
    B = list(map(int, lines[3].strip().split()))
    length, result = get_longest(A, B)
    print(f'Longest Sequence: {result}, length: {length}')

#Prgram Entry
if __name__ == "__main__":
    main()
