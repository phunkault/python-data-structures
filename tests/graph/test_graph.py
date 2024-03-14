import pytest
from src.graph.graph import Vertex


# Arrange
@pytest.fixture()
def vertex():
    return Vertex("A")


# Vertex
def test_vertex_initial_state(vertex):
    # Assert
    assert vertex
    assert vertex.id == "A"
    assert not vertex.neighbors
