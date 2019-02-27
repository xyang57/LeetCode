"""
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = []

    def push(self, x: 'int') -> 'None':
        self.items.append(x)
        try:
            old_min = self.min[-1]
            if old_min > x:
                self.min.append(x)
            else:
                self.min.append(old_min)
        except:
            self.min.append(x)
        

    def pop(self) -> 'None':
        self.min.pop()
        return self.items.pop()

    def top(self) -> 'int':
        return self.items[len(self.items)-1]

    def getMin(self) -> 'int':
        return self.min[-1]

# Time complexity: O(n); space complexity: O(n)