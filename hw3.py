"""
CMSC 14200, Spring 2023
Homework #3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""
from typing import List, Set, Dict, Tuple

from graph import Vertex, Graph


#### Task 1 ####

def num_indegree_gt_outdegree(graph: Graph) -> int:
    """
    Count how many vertices have in-degree > out-degree

    Input:
        graph (Graph): the graph

    Returns (int): the count
    """
    counts = {}
    k= 0
    for v, vert in graph.vertices.items():
        if v not in counts:
            counts[v] = 0
        for edgename in vert.edges_to:
            counts[v] -= 1
            if edgename not in counts:
                counts[edgename] = 0
            counts[edgename] += 1 
    num = 0
    for verts, ct in counts.items():
        if ct > 0:
            num += 1
    return num



#### Task 2 ####

def reachable_in(graph: Graph, vertex: str, hops: int) -> Set[str]:
    """
    Determine the set of vertices in a graph reachable from a starting point in
    at most "hops" steps

    Inputs:
        graph (Graph): the graph
        vertex (str): the name of the starting vertex
        hops (int): the maximum number of steps away from the starting point

    Returns (Set[str]): the names of vertices reachable under the constraint
    """
    explored = set(vertex)
    queue = [vertex]
    hopcount = {vertex: 0}

    while len(queue) > 0:
        point = queue.pop(0)
        for step in graph[point].edges_to:
            if step not in explored:
                explored.add(step)
                hopcount[step] = hopcount[point] + 1
            if hopcount[step] < hop:
                queue += [step]
    return len(hopcount)



#### Task 3 ####

def flood_fill(grid: List[List[bool]], start: Tuple[int, int], explored = set()) -> None:
    """
    "Flood fill" (the paint-bucket tool) a grid of booleans
    Change a cell in the grid to black (True) and its neighboring cell, and
    their neighbors, stopping when encountering an already-black (True) cell in
    a given direction
    Directions are N, E, S, and W, but not diagonal

    Inputs:
        grid (List[List[bool]]): two-dimensional grid of boolean cells
        start (Tuple[int, int]): the coordinates of the starting cell
            Returns: nothing
        """
    y, x = start
    grid[y][x] == True 
    nsew = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    k = 0
    while k < 4:
        for exp in nsew:
            yn, xn = exp
            if (yn in range(len(grid)) and xn in range(len(grid[0])) and not grid[yn][xn]):
                flood_fill(grid, exp)
            else:
                k += 1
    return None
        
    

    

