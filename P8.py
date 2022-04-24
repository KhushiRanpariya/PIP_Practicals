# 20CE118 KHUSHI RANPARIYA
# REPOSITORY LINK:
# https://github.com/KhushiRanpariya/PIP_Practicals
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()

s = Stack()
while True:
    print('1. push <value>')
    print('2. pop')
    print('3. traverse')
    print('4. quit')
    do = input('Enter the operation you want to perform. \n').split()
 
    op = do[0].strip().lower()
    if op == 'push':
        s.push(int(do[1]))
    elif op == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif op =='traverse':
        print(s.__dict__)
    elif op == 'quit':
        break
