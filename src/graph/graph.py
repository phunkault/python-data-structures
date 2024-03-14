from typing import Any


class Vertex:
    def __init__(self, v_id: Any = None) -> None:
        self.id = v_id
        self.neighbors: list[Vertex] = []
