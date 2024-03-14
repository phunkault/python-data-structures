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
