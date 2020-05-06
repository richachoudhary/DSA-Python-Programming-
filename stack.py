class stack :
    def __init__(self):
        self.stacklist=[]
    def is_empty(self):
        if (len(self.stacklist)== 0):
            return True
    def pop(self):
        if (len(self.stacklist)!= 0):
            return self.stacklist.pop()
    def push(self, val):
        self.stacklist.append(val)
    def size(self):
        return len(self.stacklist)
    def top(self):
        if (len(self.stacklist)!= 0):
            return self.stacklist[-1]

def isBalanced(exp):
    closing = ['}', ')', ']']
    st = stack()
    for character in exp:
        if character in closing:
            if st.is_empty():
                return False
            topElement = st.pop()
            if (character is '}' and topElement is not '{'):
                return False
            if (character is ')' and topElement is not '('):
                return False
            if (character is ']' and topElement is not '['):
                return False
        else:
            st.push(character)
    if (st.is_empty() is False):
        return False
    return True

if __name__ == '__main__' :
    st= stack()
    st.push(2)
    st.push(4)
    st.push(5)
    print(st.top())
    print(st.pop())

    print(isBalanced('{{{}}]'))
    print(isBalanced('{()}'))