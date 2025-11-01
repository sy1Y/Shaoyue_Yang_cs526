import sys

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0].strip()) #Number of aisles
    categories = [x.strip() for x in lines[1].split(',')]
    print(f"Input: {categories}")
    left = 0
    max_item = 0
    basket = {} #Record the quantity of each category
    for right in range(len(categories)):
        current =  categories[right]
        # Check if the category exists: if not, return 0;otherwise, count+=1
        basket[current] = basket.get(current,0) + 1

        #if it exceeds two categories, reuduce poistion
        while len(basket) > 2:
            left_current = categories[left]
            basket[left_current] -= 1 #remove poistion
            if basket[left_current] == 0:
                del basket[left_current]
            # Left pointer moves one position to the right
            left += 1
        #make sure it keeps the maximum length value
        max_item = max(max_item, right-left+1)
    print(f"{max_item} items were selected")  
    

#Program Entry
if __name__ == "__main__":
    main()
