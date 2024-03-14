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

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, vertex: "Vertex") -> bool:
        if vertex.id not in self.vertices:
            self.vertices[vertex.id] = vertex
            return True

        return False

    def get_vertices(self) -> list[Any]:
        return list(self.vertices.keys())

    def add_edge(self, vrtx1_id: Any, vrtx2_id: Any) -> bool:
        if vrtx1_id in self.vertices and vrtx2_id in self.vertices:
            self.vertices[vrtx1_id].add_neighbor(vrtx2_id)
            self.vertices[vrtx2_id].add_neighbor(vrtx1_id)
            return True

        return False
