# -*- coding: utf-8 -*-

class Stack:

    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def leek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def isEmpty(self):
        return len(self.stack) == 0

'''
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
'''
#栈的应用--括号的匹配问题
def brace_match(s):
    match = {'}':'{', ']':'[', ')':'('}
    stack = Stack()
    for ch in s:
        if ch in {'(','[','{'}:
            stack.push(ch)
        else:      #ch in {'}',']',')'}
            if stack.isEmpty():
                return False
            elif stack.leek() == match[ch]:
                stack.pop()
            else:   #stack.get_top() !=mach[ch]
                return False
    if stack.isEmpty():
        return True
    else:
        return False

print(brace_match('[{()}(){()}]'))
print(brace_match('[{(}(){()}]'))