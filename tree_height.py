# python3

import sys
import threading


def compute_height(n, parents):
    def height(node):
        if node not in cache:
            if parents[node] == -1:
                cache[node] = 1
            else:
                cache[node] = 1 + height(parents[node])
        return cache[node]

    cache = {}
    return max(height(node) for node in range(len(parents)))
    


def main():
    # newInput = input("Ievadiet 'I' ja vēlaties ievadīt no tastatūras un 'F', ja ieevade no faila:")
    while True:
        newInput = input().strip().upper()
        if newInput == "I":
            n = int(input())
            parents = list(map(int,input().split()))
            break
        elif newInput == "F":
            fileName = input()
            if "a" in fileName:
                return 1
            try:
                with open(fileName) as file:
                    n = int(file.readline())
                    parents = list(map(int, file.readline().split()))
                    break
            except FileNotFoundError:
                return 1 

    height = compute_height(n , parents)
    print(height)            

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
