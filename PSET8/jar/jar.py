

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("ValueError")
        self._cap = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n > self._cap:
            raise ValueError("ValueError")
        else:
            self._size += n
            self._cap -= n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("ValueError")
        else:
            self._size -= n
            self._cap += n
    @property
    def capacity(self):
        return self._cap

    @property
    def size(self):
        return self._size
