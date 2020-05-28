from threading import Semaphore, Lock
from collections import deque


class BoundedSynchronizedQueue:
    def __init__(self, capacity):
        self.queue = deque()
        # used to lock queue, but deque is thread-safe; therefore, actually we don't need it
        self.lock = Lock()
        self.enq = Semaphore(capacity)
        self.deq = Semaphore(0)

    def enqueue(self, val):
        self.enq.acquire()
        with self.lock:
            self.queue.append(val)
        self.deq.release()

    def dequeue(self):
        self.deq.acquire()
        with self.lock:
            ret = self.queue.popleft()
        self.enq.release()
        return ret

    def __len__(self):
        with self.lock:
            return len(self.queue)


class UnboundedSynchronizedQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = Lock()
        self.sem = Semaphore(0)

    def enqueue(self, val):
        with self.lock:
            self.queue.append(val)
        self.sem.release()

    def dequeue(self):
        self.sem.acquire()
        with self.lock:
            ret = self.queue.popleft()
        return ret

    def __len__(self):
        with self.lock:
            return len(self.queue)


if __name__ == "__main__":
    pass
