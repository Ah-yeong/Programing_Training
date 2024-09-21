class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None
        
class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
pre = []

def preorder(root):
    if root != 0:
        pre.append(root.value)
        preorder(root.left)
        preorder(root.left)

post = []

def postorder(root):
    if root != 0:
        postorder(root.left)
        postorder(root.left)
        post.append(root.value)
    
def solution(nodeinfo):
    index = []
    
    for i in range(len(nodeinfo)):
        index.append(i+1)
        
    nodeinfo.sort(key=lambda x:(x[1], x[0]))

    head = Node(nodeinfo[0][0])
    binary_tree = NodeMgmt(head)
                  
    for i in range(1, len(nodeinfo)//2):
        binary_tree.insert(nodeinfo[i][0])

    preorder(head)
    postorder(head)           
    print(pre)
    print(post)

if __name__ == "__main__":
    example = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    solution(example)
