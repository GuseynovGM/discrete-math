import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["char"])):
    def build(self, huffman_code, acc):
        huffman_code[self.char] = acc or "0"


class Tree(namedtuple("Tree", ["left", "right"])):
    def build(self, code, acc):
        self.left.build(code, acc + "0")
        self.right.build(code, acc + "1")


def encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Node(ch)))
    heapq.heapify(h)
    h_count = len(h)
    while len(h) > 1:
        freq_left, count_left, left = heapq.heappop(h)
        freq_right, count_right, right = heapq.heappop(h)
        heapq.heappush(h, (freq_left+freq_right, h_count, Tree(left, right)))
        h_count += 1
    huffman_code = {}
    if h:
        [(h_freq, h_count, root)] = h
        root.build(huffman_code, "")
    return huffman_code


if __name__ == '__main__':
    s = input()
    hfmn_code = encode(s)
    encoded = "".join(hfmn_code[e] for e in s)
    for e in sorted(hfmn_code):
        print("{}: {}".format(e, hfmn_code[e]))