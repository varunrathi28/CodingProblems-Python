# your code goes here
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorderTraversal(node):
    output = []
    postorderHelper(node, output)
    print(*output, sep= ' ')


def postorderHelper(node, output):
    if node is not None:
        postorderHelper(node.left, output)
        postorderHelper(node.right, output)
        output.append(node.data)


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
    postorderTraversal(root)