
class Solution:
    s = "()[]{}"
    def isValid(self, s: str) -> bool:
        pair = {
             "(":")" ,
             "{" :"}",
              "[":"]" ,
        }
        def isOpen(item):
            open = [ "(", "{", "[" ]
            if item in open:
                return True    
            else:
                return False

        class Node:
            def __init__(self, item,next):
                self.item = item
                self.next = next
                
        class stack:
            def __init__(self):
                self.top = None
            
            def push(self, value):
                self.top = Node(value, self.top)
            
            def pop():
                if self.top is None:
                    return None
                
                node = self.top
                self.top = self.top.next
            
            def is_empty():
                if self.top is None:
                    return None
        
        open= stack()
        
        for i in range(len(s)):
            if isOpen(s[i]):
                open.push(s[i])

        for i in range(len(s)):
            if open.top.item != pair[s[i]]:
                return False
            else:
                return True 
            


        


s1 =Solution()
s1.isValid("()[]{}")
        



        
                
                
                
            
