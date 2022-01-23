class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        ret_data = self.stack[-1]
        del self.stack[-1]
        return ret_data
    
    def isEmpty(self):
        return len(self.stack) == 0
    


C = int(input())

def open2close(char):
    if char == '(':
        return ')'
    elif char == '[':
        return ']'
    elif char == '{':
        return '}'

for _ in range(C):
    string = str(input())

    open_set = {'(', '[', '{'}
    close_set = {')', ']', '}'}
    stack = Stack()

    isMatched = True
    for char in string:
        if char in open_set:
            stack.push(char)
        elif char in close_set:
            if stack.isEmpty():
                print("NO")
                isMatched = False
                break
            
            s_char = stack.pop()
            if open2close(s_char) != char:
                print("NO")
                isMatched = False
                break
    if isMatched:
        print("YES")    