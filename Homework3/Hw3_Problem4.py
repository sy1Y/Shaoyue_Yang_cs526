filename = input("Please input the file name：").strip()

# ==== Read the file ====
def read_input(filename):
    pairs = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line or line[0].isdigit():
                continue
            data = line.split()
            bx, by = float(data[1]), float(data[2])
            gx, gy = float(data[4]), float(data[5])
            pairs.append(((bx, by), (gx, gy)))
    return pairs

# ==== Determine whether they are across ====
def lines_intersect_or_coincident(A, B, C, D, eps=1e-9):
    d1x = B[0] - A[0]
    d1y = B[1] - A[1]
    d2x = D[0] - C[0]
    d2y = D[1] - C[1]

    # Cross product
    cross = d1x * d2y - d1y * d2x
    if abs(cross) > eps:
        return True
    else:
        # Parallel，check collinear
        cross2 = (C[0] - A[0]) * d1y - (C[1] - A[1]) * d1x
        if abs(cross2) < eps:
            # collinear,intersect
            return True
        else:
            # Parallel&not collinear, not intersect
            return False

def check_any_line_intersection(pairs):
    n = len(pairs)
    for i in range(n):
        for j in range(i + 1, n):
            A, B = pairs[i]
            C, D = pairs[j]
            if lines_intersect_or_coincident(A, B, C, D):
                # If any two lines intersect or overlap,fails
                return True
    return False

pairs = read_input(filename)
has_intersection = check_any_line_intersection(pairs)

if has_intersection:
    print("All Ghosts: were not eliminated")
else:
    print("All Ghosts: were eliminated")
