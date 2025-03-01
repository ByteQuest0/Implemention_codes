import heapq

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if not text:
        return None

    frequency = {}
    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1

    heap = [Node(freq, char=char) for char, freq in frequency.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        node = heap[0]
        return Node(node.freq, left=node)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(node1.freq + node2.freq, left=node2, right=node1)
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node is None:
        return code_map

    if node.char is not None:
        code_map[node.char] = prefix or "1"
    else:
        build_codes(node.left, prefix + "1", code_map)
        build_codes(node.right, prefix + "0", code_map)
    return code_map

def huffman_encoding(text):
    if text == "":
        return "", None

    root = build_huffman_tree(text)
    codes = build_codes(root)
    encoded_text = "".join(codes[ch] for ch in text)
    return encoded_text, root, codes

def huffman_decoding(encoded_text, root):
    if not encoded_text or root is None:
        return ""

    decoded_text = ""
    node = root

    if root.left is None and root.right is None:
        return root.char * len(encoded_text)

    for bit in encoded_text:
        node = node.left if bit == '1' else node.right

        if node.char is not None:
            decoded_text += node.char
            node = root

    return decoded_text

def calculate_table_size(codes):
    # Each entry stores a character and its corresponding code
    size = 0
    for char, code in codes.items():
        size += 8  # 1 byte to store the character
        size += len(code)  # bits for the code itself
    return size

if __name__ == "__main__":
    text = 'BANANA BANDANA'

    print("Original text: \n", text)
    original_size_bits = len(text) * 8
    print("Size of original text (in bits):", original_size_bits)

    encoded, tree, codes = huffman_encoding(text)
    print("\nEncoded text:", encoded)
    encoded_size_bits = len(encoded)
    print("Size of encoded text (in bits):", encoded_size_bits)

    table_size_bits = calculate_table_size(codes)
    total_compressed_size = encoded_size_bits + table_size_bits

    print("Size of the Huffman table (in bits):", table_size_bits)
    print("Total size of compressed file (encoded text + table):", total_compressed_size)

    decoded = huffman_decoding(encoded, tree)
    print("\nDecoded text:", decoded)
    decoded_size_bits = len(decoded) * 8
    print("Size of decoded text (in bits):", decoded_size_bits)
