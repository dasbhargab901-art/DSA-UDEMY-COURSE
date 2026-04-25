# Unlike Binary Tree, it can have multiple children
class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + "-" + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


drinks = TreeNode("Drinks", [])
hot = TreeNode("Hot", [])
cold = TreeNode("Cold", [])

# cold's children
coke = TreeNode("Coke", [])
fanta = TreeNode("Fanta", [])

# hot's children
coffee = TreeNode("Coffee", [])
tea = TreeNode("Tea", [])

drinks.addChild(hot)
drinks.addChild(cold)

cold.addChild(fanta)
cold.addChild(coke)

hot.addChild(tea)
hot.addChild(coffee)

print(drinks)
