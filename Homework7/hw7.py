import sys
import heapq
from collections import Counter
import struct

class HuffmanNode:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.freq = frequency
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

   #Display binary tree
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
        #leaf node: show charaters and frequencies
        if self.symbol is not None:
            if self.symbol == ' ':
                char_display = "[SPACE]"
            elif self.symbol == '\n':
                char_display = "[NEWLINE]"
            elif self.symbol == '\t':
                char_display = "[TAB]"
            else:
                char_display = f"'{self.symbol}'"
            line = f"{char_display}:{self.freq}"
            width = len(line)
            return [line], width, 1, width // 2

        if not self.right: #only left childnode
            left_lines, n, p, x = self.left.display()
            s = f"{self.freq}"
            return construct_lines(s, left_lines, [], n, p, x, 0, 0, 0), n + len(s), p + 2, n + len(s) // 2
        if not self.left:  #only right childnode
            right_lines, m, q, y = self.right.display()
            s = f"{self.freq}"
            return construct_lines(s, [], right_lines, 0, 0, 0, m, q, y), m + len(s), q + 2, len(s) // 2
        #both 
        left_lines, n, p, x = self.left.display()
        right_lines, m, q, y = self.right.display()
        s = f"{self.freq}"
        return construct_lines(s, left_lines, right_lines, n, p, x, m, q, y), n + m + len(s), max(p, q) + 2, n + len(s) // 2

#encoding
def encode_main():
    input_text = sys.stdin.read()
    print("\n1. Input text:")
    print(input_text[:100] + ("..." if len(input_text) > 100 else ""))

    freq_map = Counter(input_text) #create frequency map
    print("\n2. Frequency Map:")
    for char, freq in sorted(freq_map.items()):
        display_char = repr(char)[1:-1]
        print(f"'{display_char}': {freq}")

    def build_huffman_tree(frequency_table): #build huffman binary tree
        heap = [HuffmanNode(char, freq) for char, freq in frequency_table.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            parent = HuffmanNode(None, left.freq + right.freq)
            parent.left, parent.right = left, right
            heapq.heappush(heap, parent)    
        return heap[0] if heap else None
    root = build_huffman_tree(freq_map)
    def generate_codes(node, code="", codes=None):
        if codes is None:
            codes = {}
        if node:
            if node.symbol is not None:
                codes[node.symbol] = code
            generate_codes(node.left, code + "0", codes)
            generate_codes(node.right, code + "1", codes)
        return codes
    huffman_codes = generate_codes(root)
    print("\n3. Huffman Tree:")
    tree_lines, _, _, _ = root.display()
    for line in tree_lines:
        print(line)
    print("\n4. Huffman Codes:")
    for char, code in sorted(huffman_codes.items(), key=lambda x: len(x[1])):
        char_display = repr(char)[1:-1]
        print(f"'{char_display}': {code}")

    #encode text
    encoded_text = ''.join(huffman_codes[char] for char in input_text)
    # Write compressed file
    with open("compressed.bin", "wb") as f:
        f.write(struct.pack("I", len(huffman_codes)))
        for char, code in huffman_codes.items(): #save codebook
            f.write(struct.pack("I", ord(char)))
            f.write(struct.pack("B", len(code)))
            f.write(code.encode())
        f.write(struct.pack("I", len(encoded_text))) #save encoded text length
        padding = (8 - len(encoded_text) % 8) % 8
        encoded_text += '0' * padding
        for i in range(0, len(encoded_text), 8):
            byte = int(encoded_text[i:i+8], 2)
            f.write(struct.pack("B", byte))
    print("   Compressed file saved as: compressed.bin")

#decoding
def decode_main():
    print("\n=== Huffman Decoding ===")
    with open("compressed.bin", "rb") as f:
        num_codes = struct.unpack("I", f.read(4))[0]
        huffman_codes = {}
        for _ in range(num_codes):
            char_int = struct.unpack("I", f.read(4))[0]
            code_len = struct.unpack("B", f.read(1))[0]
            code = f.read(code_len).decode()
            huffman_codes[chr(char_int)] = code
        encoded_len = struct.unpack("I", f.read(4))[0]
        encoded_bits = ""
        while len(encoded_bits) < encoded_len:
            byte = struct.unpack("B", f.read(1))[0]
            encoded_bits += format(byte, "08b")
        encoded_bits = encoded_bits[:encoded_len]
    # Rebuild tree from codes
    def build_tree_from_codebook(codebook):
        root = HuffmanNode()
        for char, code in codebook.items():
            node = root
            for bit in code:
                if bit == "0":
                    if not node.left:
                        node.left = HuffmanNode()
                    node = node.left
                else:
                    if not node.right:
                        node.right = HuffmanNode()
                    node = node.right
            node.symbol = char  # Leaf node
        return root
    root = build_tree_from_codebook(huffman_codes)
    print("\nReconstructed Huffman Tree:")
    tree_lines, _, _, _ = root.display()
    for line in tree_lines:
        print(line)
    #decode text
    decoded = []
    node = root
    for bit in encoded_bits:
        node = node.left if bit == "0" else node.right
        if node.symbol is not None:
            decoded.append(node.symbol)
            node = root
    decoded_text = "".join(decoded)
    print("\nDecoded text:")
    print(decoded_text[:100] + ("..." if len(decoded_text) > 100 else ""))
    #save output
    with open("reconstructed.txt", "w") as f:
        f.write(decoded_text)
    print("   Reconstructed file saved as: reconstructed.txt")

def main():
    encode_main()
    print("\n" + "=" * 60)
    decode_main()
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
