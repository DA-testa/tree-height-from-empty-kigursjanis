import sys
import threading


def calculate_tree_height(num_nodes, node_parents):
    children = [[] for _ in range(num_nodes)]
    for i in range(num_nodes):
        parent = node_parents[i]
        if parent == -1:
            root = i
        else:
            children[parent].append(i)
 
    def compute_depth(node):
        if not children[node]:
            return 1
        max_depth = 0
        for child in children[node]:
            depth = compute_depth(child)
            max_depth = max(max_depth, depth)
        return max_depth + 1

    return compute_depth(root)


def main():
    input_type = input().strip()

    if 'I' in input_type:
        num_nodes = int(input().strip())
        node_parents = list(map(int, input().strip().split()))
        tree_height = calculate_tree_height(num_nodes, node_parents)
        print(tree_height)
    elif 'F' in input_type:
        file_name = input().strip()
        with open("test/" + file_name, 'r') as f:
            num_nodes = int(f.readline().strip())
            node_parents = list(map(int, f.readline().strip().split()))
            tree_height = calculate_tree_height(num_nodes, node_parents)
            print(tree_height)
    else:
        print("invalid input")
        exit()

if __name__ == '__main__':
    sys.setrecursionlimit(10**7) 
    threading.stack_size(2**27)  
    threading.Thread(target=main).start()
