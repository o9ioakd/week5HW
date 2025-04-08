#1
class ListQueue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, x):
        self.__queue.insert(0, x)

    def dequeue(self):
        return self.__queue.pop()

    def front(self):
        return self.__queue[-1]

    def is_empty(self) -> bool:
        return len(self.__queue) == 0

    def dequeueAll(self):
        self.__queue.clear()


#2
def is_w_dollar_w(s: str) -> bool:
    if '$' not in s:
        return False

    w1, w2 = s.split('$', 1)
    queue = []
    for ch in w1:
        queue.append(ch)
    for ch in reversed(w2):
        if not queue or queue.pop(0) != ch:
            return False

    return len(queue) == 0

#3
def copy_linked_queue(a):
    b = LinkedQueue()
    for i in range(a._LinkedQueue__queue.size()):
        item = a._LinkedQueue__queue.get(i)
        b.enqueue(item)
    return b

#4
class StackUsingQueues:
    def __init__(self):
        self.q1 = []
        self.q2 = []
    def is_empty(self):
        return len(self.q1) == 0
    def push(self, x):
        self.q1.append(x)
    def pop(self):
        if self.is_empty():
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        top = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return top

    def top(self):
        if self.is_empty():
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        top = self.q1.pop(0)
        self.q2.append(top)
        self.q1, self.q2 = self.q2, self.q1
        return top


#5
class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    def is_empty(self):
        return len(self.stack_in) == 0 and len(self.stack_out) == 0
    def enqueue(self, x):
        self.stack_in.append(x)
    def dequeue(self):
        if self.is_empty():
            return None
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def front(self):
        if self.is_empty():
            return None
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]


#6
'''
원형 연결 리스트 기반 Deque에서는 모든 enqueue/dequeue 연산이 O(1) 시간에 수행된다.
(큐의 크기 n과 무관)
'''

#7
'''
enqueue() 연산은 다음 두 경우로 나눌 수 있다:
Deque의 front에서 수행할 경우: insert(0, x)를 통해 Θ(1)의 시간으로 수행 가능하다.
Deque의 tail에서 수행할 경우: 리스트의 맨 끝까지 순회 후 삽입하게 되므로 Θ(n)의 시간이 소요된다.
따라서, enqueue()의 수행 시간은 최악의 경우를 고려하여 Θ(n) 이다.

dequeue() 연산도 다음과 같이 나눌 수 있다:
Deque의 front에서 수행할 경우: pop(0) 연산을 통해 Θ(1)의 시간으로 수행 가능하다.
Deque의 tail에서 수행할 경우: 리스트를 끝까지 순회하여 이전 노드를 찾아야 하므로 Θ(n)의 시간이 소요된다.
따라서, dequeue()의 수행 시간도 최악의 경우를 고려하여 Θ(n) 이다.
'''

#8
class ListDeque:
    def __init__(self):
        self.__deque = []

    def enqueueRear(self, x):
        self.__deque.append(x)
    def enqueueFront(self, x):
        self.__deque.insert(0, x)
    def dequeueFront(self):
        if self.isEmpty():
            return None
        return self.__deque.pop(0)
    def dequeueRear(self):
        if self.isEmpty():
            return None
        return self.__deque.pop()
    def front(self):
        if self.isEmpty():
            return None
        return self.__deque[0]
    def rear(self):
        if self.isEmpty():
            return None
        return self.__deque[-1]
    def isEmpty(self) -> bool:
        return len(self.__deque) == 0
    def dequeueAll(self):
        self.__deque.clear()
    def printDeque(self):
        print("Deque from front to rear:", end=' ')
        for item in self.__deque:
            print(item, end=' ')
        print()
