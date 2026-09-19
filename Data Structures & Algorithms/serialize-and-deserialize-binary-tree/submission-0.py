# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        ans = []
        
        def preOrder(root):
            if not root:
                ans.append('#')
                return

            ans.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)

            return
            
        preOrder(root)
        return ",".join(ans)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(',')
        i = 0

        def build():
            nonlocal i

            value = values[i]
            i += 1

            if value == '#':
                return None
            
            node = TreeNode(int(value))

            node.left = build()
            node.right = build()

            return node
        
        return build()
















