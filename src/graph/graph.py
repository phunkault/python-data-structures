from typing import Any


class Vertex:
    def __init__(self, v_id: Any = None) -> None:
        self.id = v_id
        self.neighbors: list[Vertex] = []

    def add_neighbor(self, neighbor: "Vertex") -> None:
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)


class Graph:
    def __init__(self):
        self.vertices: dict[Any, Vertex] = {}
