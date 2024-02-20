class LFUCache:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._size: int = 0
        self._min_freq: int = 1
        self._node_map: dict = {}
        self._freq_map: dict = {}
        self._buckets: dict = {}

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    def put(self):
        pass

    def get(self):
        pass
