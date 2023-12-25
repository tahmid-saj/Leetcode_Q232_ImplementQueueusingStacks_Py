class MyQueue(object):

    # pop, append, len

    def __init__(self):
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.list) == 0:
            self.list.append(x)
        else:
            list2 = [x]
            for i in range(len(self.list)):
                list2.append(self.list[i])
            self.list = list2

    def pop(self):
        """
        :rtype: int
        """
        # remove -1 index
        return self.list.pop()

    def peek(self):
        """
        :rtype: int
        """
        # return -1 index
        return self.list[-1]

    def empty(self):
        """
        :rtype: bool
        """
        # return len(list)
        return len(self.list) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
