import pytest
from src.graph.graph import Vertex


# Arrange
@pytest.fixture()
def vertexA():
    return Vertex("A")


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
