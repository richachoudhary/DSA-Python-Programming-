from Node import Node
class LinkedList:
    def __init__(self):
        self.head_node= None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is not None:
            return False
        else :
            return True

    def insert_at_head(self, data):
        temp = Node(data)
        # if self.head_node== None:
        #     return temp
        temp.next= self.head_node
        self.head_node = temp
        return self.head_node


### supp linkedlist  print####
    def printlinkedlist(self):
        if (self.is_empty()):
            print("Linkedlist is empty")
            return False
        temp = self.head_node
        while (temp.next is not None):
            print (temp.data, end=  " -> ")
            temp= temp.next
        print (temp.data, end= "-> Null")
        return True



def insert_at_tail(list, data):
    node = Node(data)
    temp = list.get_head()
    if temp is None :
        return node
    while (temp.next is not None ):
        temp = temp.next
    temp.next = node
    return


def length_of_ll(list):
    count = 0
    temp = list.get_head()
    if temp is None :
        print ("empty ll")
        return
    while temp is not None :
        temp = temp.next
        count += 1
    return count

def reverse_ll(list):
    current = list.get_head()
    prev= None
    while (current is not None ):
        temp = current.next
        current.next= prev
        prev= current
        current= temp
    list.head_node= prev

def add_two_ll(list1, list2):


if __name__ == '__main__':
    ls = LinkedList()
    ls.printlinkedlist()
    for i in range(1, 12):
        ls.insert_at_head(i)

    insert_at_tail(ls, 0)
    insert_at_tail(ls, -1)
    insert_at_tail(ls, 100)

    ls.printlinkedlist()
    print (" ")
    print (length_of_ll(ls))

    reverse_ll(ls)
    ls.printlinkedlist()