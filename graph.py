"""
CMSC 14200, Spring 2023
Homework #3

Do not modify this file!
"""
from typing import Optional, Dict

class Vertex:
    """
    Class for representing a vertex in an unweighted, directed graph
    """

    name : str
    edges_to : Dict[str, "Vertex"]

    def __init__(self, name: str):
        """
        Constructor

        Parameters:
            name : str : name for the vertex
        """
        self.name = name
        self.edges_to = {}

    def add_edge_to(self, dest: "Vertex") -> None:
        """
        Adds edge from this vertex to another

        Parameters:
            dest : Vertex : vertex to which to add an edge

        Returns: nothing
        """
        self.edges_to[dest.name] = dest

    def __str__(self) -> str:
        """
        Produce a string representation of a Vertex with the name and list of
        neighbors

        Parameters: none beyond self

        Returns: str
        """
        rv = f"Vertex {self.name}:"
        neighbors = ", ".join(sorted(self.edges_to.keys()))
        return rv + " edges: " + neighbors


class Graph:
    """
    Class for representing an entire unweighted, directed graph
    """

    vertices : Dict[str, Vertex]

    def __init__(self, filename: Optional[str] = None):
        """
        Constructor

        Parameters:
            filename : None or str : base name for CSV files
                                     representing a graph
        """
        self.vertices = {}

        if filename:
            with open(filename + ".vertices", encoding="utf8") as f:
                for line in f:
                    name = line.strip()
                    v = Vertex(name)
                    self.add_vertex(v)

            with open(filename + ".edges", encoding="utf8") as f:
                for line in f:
                    origin, destination = line.strip().split(",")
                    origin_v = self.get_vertex(origin)
                    destination_v = self.get_vertex(destination)
                    assert origin_v
                    assert destination_v
                    origin_v.add_edge_to(destination_v)

    def add_vertex(self, vertex: Vertex) -> None:
        """
        Adds vertex to graph

        Parameters:
            vertex : Vertex : vertex to be added

        Returns: nothing
        """
        self.vertices[vertex.name] = vertex

    def get_vertex(self, name: str) -> Optional[Vertex]:
        """
        Looks up vertex in graph

        Parameters:
            name : str : name of sought vertex

        Returns: Vertex or None (if not found)
        """
        return self.vertices.get(name)
