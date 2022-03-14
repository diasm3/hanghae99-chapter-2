class Node:
    def __init__(self, item, next):
        self.item = item ##item 값을 넣는다
        self.next = next ##next가 가리키고 있는 것을 다음 넥스트로 또 가리킨다. 


class Stack:
    def __init__(self):
        self.top = None ## 무조건 스택이 콜되면 init 가 먼저 불러온다 . 그러면 self.top 입구를 만들어서 초기화 해라 

    def push(self, value):  
        self.top = Node(value, self.top) ##탑에다가 노드 객체를 넣는다. 

    def pop(self):
        if self.top is None: ##만약 에 빈 스택이면 
            return None ##None 을 리턴해줘라 

        node = self.top ## 빈 스택이 아닐 경우에는  node에 최상위에 있는 top 객체를 불러와라 
        self.top = self.top.next ## 최상위에 밑에 있는 next를 받아서 다시 self.top객체에다가 연결 시켜줘라 

        return node.item #아까 뽑았던 node객체 안에 item을 받아서 리턴해줘라

    def is_empty(self):
        return self.top is None #Top이 비어있는지 확인 
    



stack1 = Stack()

for i in range(5):
    stack1.push(i)
    
assert stack1.pop()
print("complete")