import sys
import threading
import numpy

def compute_height(n, parents):
    tree = {}
    for node, parent in enumerate(parents):
        if parent == -1:
            continue
        if parent not in tree:
            tree[parent] = [node]
        else:
            tree[parent].append(node)

    def height(node):
        if node not in tree:
            return 1
      
        heights = [height(child) for child in tree[node]]
 
        return max(heights) + 1
    root = parents.index(-1)
    return height(root)

def main():
    print("Input from k(keyboard) or k(file)? (k/f)")
    source = input().strip().lower()
    while source not in ['k', 'f']:
        print("Input error")
        source = input().strip().lower()
        if source == 'k':
            print("Number of nodes:")
        n = int(input())

        print("Parents of nodes")
        parents = list(map(int, input().split()))
    else:
        print("Filename:")
        filename = input().strip()
        if 'a' in filename:
            print("Error retrieving filename")
            return
        try:
            with open(f'folder/{filename}', 'r') as f:
               
                n = int(f.readline().strip())
               
                parents = list(map(int, f.readline().strip().split()))
        except:
            print("Error reading file.")
            return
    print("Tree Height:", compute_height(n, parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start() 
