import pytest
from src.graph.graph import Vertex, Graph


# Arrange
@pytest.fixture()
def vertexA():
    return Vertex("A")


@pytest.fixture()
def graph():
    return Graph()


# Vertex
def test_vertex_initial_state(vertexA):
    # Assert
    assert vertexA
    assert vertexA.id == "A"
    assert not vertexA.neighbors


def test_add_vertex_neighbors(vertexA):
    # Arrange
    vertexB = Vertex("B")
    vertexC = Vertex("C")

    # Act
    vertexA.add_neighbor(vertexB)
    vertexA.add_neighbor(vertexC)

    # Assert
    assert len(vertexA.neighbors) == 2
    assert vertexB in vertexA.neighbors
    assert vertexC in vertexA.neighbors


# Graph
def test_graph_initial_state(graph):
    # Assert
    assert graph
    assert not graph.vertices


def test_add_unique_vertex_to_graph(graph):
    # Arrange
    vertex = Vertex("A")

    # Act
    graph.add_vertex(vertex)

    # Assert
    assert len(graph.vertices) == 1
    assert vertex.id in graph.vertices


def test_add_vertex_duplicate_to_graph(graph):
    # Arrange
    vertex = Vertex("A")
    graph.add_vertex(vertex)

    # Act
    graph.add_vertex(vertex)

    # Assert
    assert len(graph.vertices) == 1
    assert vertex.id in graph.vertices


def test_add_multiple_vertices_to_graph(graph):
    # Arrange
    vertexA = Vertex("A")
    vertexB = Vertex("B")
    vertexC = Vertex("C")

    # Act
    graph.add_vertex(vertexA)
    graph.add_vertex(vertexB)
    graph.add_vertex(vertexC)

    # Assert
    assert len(graph.vertices) == 3
    assert vertexA.id in graph.vertices
    assert vertexB.id in graph.vertices
    assert vertexC.id in graph.vertices


def test_get_vertices(graph):
    # Arrange
    vertexA = Vertex("A")
    vertexB = Vertex("B")
    vertexC = Vertex("C")

    graph.add_vertex(vertexA)
    graph.add_vertex(vertexB)
    graph.add_vertex(vertexC)

    # Act and Assert
    vertices = graph.get_vertices()

    assert len(vertices) == 3
    assert "A" in vertices
    assert "B" in vertices
    assert "C" in vertices


def test_add_edge_existing_vertices(graph):
    # Arrange
    vertexA = Vertex("A")
    vertexB = Vertex("B")
    graph.add_vertex(vertexA)
    graph.add_vertex(vertexB)

    # Act and Assert
    assert graph.add_edge("A", "B") is True
    assert "B" in graph.vertices["A"].neighbors
    assert "A" in graph.vertices["B"].neighbors


def test_add_edge_non_existing_vertices(graph):
    # Act and Assert
    assert graph.add_edge("A", "D") is False
    assert not graph.vertices.get("A")
    assert not graph.vertices.get("D")


def test_add_edge_with_one_existing_vertex(graph):
    # Arrange
    vertexD = Vertex("D")
    graph.add_vertex(vertexD)

    # Act and Assert
    assert graph.add_edge("A", "D") is False


def test_add_edge_with_no_vertices(graph):
    assert graph.add_edge("A", "B") is False
