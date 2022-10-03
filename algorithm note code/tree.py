class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# 전위순회
def preorder(root):
    if root is not None:
        print (root.key,end=" ")
        inorder(root.left)
        inorder(root.right)
  
# 중위순회
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.key,end=" ")
        inorder(root.right)
  
# 후위순회
def postorder(root):
    if root is not None:
        inorder(root.left)
        inorder(root.right)
        print (root.key,end=" ")
  
# 노드 삽입
def insert(node, key):
    if node is None:
        return Node(key)
  
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
        
    return node

# 리프노드 중 최소값 찾기
def minValueNode(node):
    current = node
  
    while(current.left is not None):
        current = current.left
  
    return current

#노드 삭제
def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
  
    elif(key > root.key):
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
  
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
  
    return root
  

'''
BST
          50
       /     \
      30      70
     /  \    /  \
   20   40  60   80 

'''
  
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
  
print ("Inorder traversal")
inorder(root)

print ("\npreorder traversal")
preorder(root)

print ("\npostorder traversal")
postorder(root)
  
print ("\nDelete 20")
root = deleteNode(root, 20)
print ("Inorder traversal")
inorder(root)
  
print ("\nDelete 30")
root = deleteNode(root, 30)
print ("Inorder traversal")
inorder(root)
  
print ("\nDelete 50")
root = deleteNode(root, 50)
print ("Inorder traversal")
inorder(root)
