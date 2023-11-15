class Node:
    def __init__(self, key, parent=None, left=None, right=None, color='RED'):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    def __str__(self):
        return str(self.key)

class RBTree:
    def __init__(self):
        self.nil = Node(None, color='BLACK')
        self.root = self.nil
    
    def print_tree(self, node=None, indent="", last=True):
        if node is None:
            node = self.root

        if node is not self.nil:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "

            print(node.key, node.color)
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)
    
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left is not self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
    
    def _right_rotate(self, y):
        x = y.left
        y.left = x.right

        if x.right is not self.nil:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is self.nil:
            self.root = x
        elif y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        
        x.right = y
        y.parent = x
    
    def insert(self, value):
        z = Node(value)
        y = self.nil
        x = self.root

        while x is not self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        
        z.parent = y

        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        
        z.left = self.nil
        z.right = self.nil
        z.color = 'RED'
        self._insert_fixup(z)
    
    def _insert_fixup(self, z):
        while z.parent.color == 'RED':
            if z.parent is z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self._left_rotate(z.parent.parent)
        self.root.color = 'BLACK'
    
    def transplant(self, u, v):
        if u.parent is self.nil:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        
        v.parent = u.parent
    
    def tree_minimum(self, x):
        while x.left is not self.nil:
            x = x.left
        return x
    
    def remove(self, z):
        y = z
        x = Node(None)
        y_original_color = y.color
        if(z.left is self.nil):
            x = z.right
            self.transplant(z, z.right)
        elif(z.right is self.nil):
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'BLACK':
            self._remove_fixup(x)
    
    def _remove_fixup(self, x):
        w = Node(None)
        while x is not self.root and x.color == 'BLACK':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.right.color == 'BLACK':
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.left.color == 'BLACK':
                        w.right.color = 'BLACK'
                        w.color = 'RED'
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 'BLACK'

if __name__ == "__main__":
    my_tree = RBTree()

    my_tree.insert(10)
    my_tree.insert(5)
    my_tree.insert(3)
    my_tree.insert(7)
    my_tree.insert(15)
    my_tree.insert(12)
    my_tree.insert(20)

    my_tree.print_tree()
    
    # pause program
    input("Press Enter to continue...")

    my_tree.remove(my_tree.root.left)
    my_tree.print_tree()
