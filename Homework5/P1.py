import sys
import random

class Node:
    #set pointer
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    def display(self):
        def construct_lines(s, left_lines, right_lines, n, p, x, m, q, y):
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left_lines += [n * ' '] * (q - p)
            elif q < p:
                right_lines += [m * ' '] * (p - q)
            return [first_line, second_line] + [a + u * ' ' + b for a, b in zip(left_lines, right_lines)]
        if not self.left and not self.right:
            line = f"{self.value}"
            width = len(line)
            return [line], width, 1, width // 2
        if not self.right:
            left_lines, n, p, x = self.left.display()
            s = f"{self.value}"
            return construct_lines(s, left_lines, [], n, p, x, 0, 0, 0), n + len(s), p + 2, n + len(s) // 2
        if not self.left:
            right_lines, m, q, y = self.right.display()
            s = f"{self.value}"
            return construct_lines(s, [], right_lines, 0, 0, 0, m, q, y), m + len(s), q + 2, len(s) // 2
        left_lines, n, p, x = self.left.display()
        right_lines, m, q, y = self.right.display()
        s = f"{self.value}"
        return construct_lines(s, left_lines, right_lines, n, p, x, m, q, y), n + m + len(s), max(p, q) + 2, n + len(s) // 2
    
#ADT for binary search tree
class BST:
    def __init__(self):
        self.root = None
        
    def add_node(self, value):
        new_node = Node(value) #add a new node with the given value
        if self.root is None:
            self.root = new_node # Set the first node as the root node
            return True
        current = self.root #search from root if tree is non-empty
        #search downward in the tree until empty space is found
        while current is not None:
            if value < current.value: #add smaller value
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            elif value > current.value: #add bigger value
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right
            else: #value already exists
                return False
            
    def delete_node(self, value):
        current = self.root #search from root
        parent = None
        #find the node to delete
        while current is not None and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        #No node to be deleted found
        if current is None:
            return False
        #deletion based on childnode: deleted value without childnode
        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
        #deleted value with only one childnode
        elif current.left is None: #only has right childnode
            if current == self.root:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
        elif current.right is None: #only has left childnode
            if current == self.root:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
        else:
#deleted value with two childnodes - replace with min value from right sub-tree
            sucessor_parent = current
            sucessor = current.right
            while sucessor.left is not None:
                sucessor_parent = sucessor
                sucessor = sucessor.left
            current.value = sucessor.value
            if sucessor_parent.left == sucessor:
                sucessor_parent.left = sucessor.right
            else:
                sucessor_parent.right = sucessor.right
        return True
    
    def find_node(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def print_tree(self):
        if self.root is None:
            print("The tree is empty.")
            return
        lines, _, _, _ = self.root.display()
        for line in lines:
            print(line)
            
def main():
    #Generate a random input set (5-50 numbers, range:1-1000)
    input_size = random.randint(5, 50)
    input_set = random.sample(range(1, 1001), input_size)
    print("Initial Input Set:", input_set)
    bst = BST()
    for val in input_set:
        bst.add_node(val)
    print("\nInitial Tree:")
    bst.print_tree()
    
    #Test add node
    new_val = random.randint(1,1000)
    print(f"\nAdding node: {new_val}")
    bst.add_node(new_val)
    bst.print_tree()

    #Test delete node
    del_val = random.choice(input_set)
    print(f"\nDeleting node: {del_val}")
    bst.delete_node(del_val)
    bst.print_tree()

    #Test find(positive case)
    find_val = random.choice(input_set)
    found = bst.find_node(find_val)
    print(f"\nFinding {find_val}: {'Found' if found else 'Not Found'}")
    #(negative case)
    not_exist = random.randint(1001, 2000)
    found2 = bst.find_node(not_exist)
    print(f"Finding {not_exist}: {'Found' if found2 else 'Not Found'}")
    
#Prgram Entry
if __name__ == "__main__":
    main()
