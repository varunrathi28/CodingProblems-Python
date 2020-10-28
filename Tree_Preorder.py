# your code goes here
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorderTraversal(node):
    output = []
    preorderHelper(node, output)
    print(*output, sep= ' ')


def preorderHelper(node, output):
    if node is not None:
        output.append(node.data)
        preorderHelper(node.left, output)
        preorderHelper(node.right, output)


t = int(input())
for _ in range(t):
    N = int(input())
    nums = [int(j) for j in input().split()]
    nodes = []
    for num in nums:
        node = Node(num)
        nodes.append(node)

    for i in range(1, N):
        inputArr = []
        inputArr = [int(k) for k in input().split()]
        parent, child, isRight = inputArr[0], inputArr[1], inputArr[2]
        if isRight == 0:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]

    root = nodes[0]
    preorderTraversal(root)