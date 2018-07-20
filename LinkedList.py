


class Node():
    def __init__(self, _object, next_node= None, copy_node=None):
        self.object=_object
        self.next_node=next_node
        if copy_node is not None:
            self.object=copy_node.object
            self.next_node=copy_node.next_node


    def to_string(self):
        ''' TODO: could have moved to an utility function... '''
        current_node = self
        while current_node.next_node is not None:
            print(current_node.object)
            current_node=current_node.next_node
        print(current_node.object)


def reverse(node3):
    new_node=Node(node3.object)
    current_node=node3
    while current_node.next_node is not None:
        current_node=current_node.next_node
        new_node=Node(current_node.object, new_node)
    return new_node



def tail(node3, n):
    ''' Last n element: TODO: if we have <n elements... '''
    current_node=node3
    i=0

    new_tail=None
    while current_node.next_node is not None:
        current_node=current_node.next_node
        i+=1
        if i>=n:
            new_tail=Node(current_node.object, new_tail)
    if i<n:
        return node3

    return new_tail


node1=Node('1')
node2=Node('2', node1)
node3=Node('3', node2)
node4=Node('4', node3)
node4.to_string()
print('---------')
reverse(node4).to_string()
print('---------')
tail(node4, 2).to_string()
print('---------')
tail(node4, 6).to_string()
