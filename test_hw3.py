import json
from hw3 import *
from graph import *

def test_task1_1() -> None:
    degree_helper(1, 1)

def test_task1_2() -> None:
    degree_helper(2, 0)

def test_task1_3() -> None:
    degree_helper(3, 2)

def test_task1_4() -> None:
    degree_helper(4, 3)

def test_task1_5() -> None:
    degree_helper(5, 2)

def test_task1_6() -> None:
    degree_helper(6, 4)

def test_task1_7() -> None:
    degree_helper(7, 1)

def test_task1_8() -> None:
    degree_helper(8, 5)

def test_task1_9() -> None:
    degree_helper(9, 6)

def test_task1_10() -> None:
    degree_helper(10, 0)

def test_task1_11() -> None:
    degree_helper(11, 1)

def test_task1_12() -> None:
    degree_helper(12, 1)

def test_task2_1() -> None:
    reachable_helper(1, "ring0", 0)

def test_task2_2() -> None:
    reachable_helper(1, "ring0", 1)

def test_task2_3() -> None:
    reachable_helper(1, "ring0", 2)

def test_task2_4() -> None:
    reachable_helper(1, "ring0", 3)

def test_task2_5() -> None:
    reachable_helper(2, "ring0", 3)

def test_task2_6() -> None:
    reachable_helper(3, "ring3-0111", 0)

def test_task2_7() -> None:
    reachable_helper(3, "ring3-0111", 1)

def test_task2_8() -> None:
    reachable_helper(3, "ring3-0111", 2)

def test_task2_9() -> None:
    reachable_helper(3, "ring3-0111", 3)

def test_task2_10() -> None:
    reachable_helper(4, "ring3-0111", 1)

def test_task2_11() -> None:
    reachable_helper(4, "ring3-0111", 2)

def test_task2_12() -> None:
    reachable_helper(4, "ring3-0111", 3)

def test_task3_1() -> None:
    flood_helper(1)

def test_task3_2() -> None:
    flood_helper(2)

def test_task3_3() -> None:
    flood_helper(3)

def test_task3_4() -> None:
    flood_helper(4)

def test_task3_5() -> None:
    flood_helper(5)

def test_task3_6() -> None:
    flood_helper(6)

def test_task3_7() -> None:
    flood_helper(7)

def test_task3_8() -> None:
    flood_helper(8)

def test_task3_9() -> None:
    flood_helper(9)

def test_task3_10() -> None:
    flood_helper(10)

def test_task3_11() -> None:
    flood_helper(11)

def test_task3_12() -> None:
    flood_helper(12)


def degree_helper(test: int, correct: int) -> None:
    filename = f"tests/degree-{test}"
    graph = Graph(filename)
            
    assert num_indegree_gt_outdegree(graph) == correct

def reachable_helper(test: int, start: str, hops: int) -> None:
    filename = f"tests/reachable-{test}"
    graph = Graph(filename)
    correct = set()
    with open(filename + f"-{hops}.set") as f:
        for line in f:
            correct.add(line.strip())
            
    assert reachable_in(graph, start, hops) == correct

def flood_helper(test: int) -> None:
    with open(f"tests/flood-{test}.json") as f:
        data = json.load(f)
        
        flood_fill(data["before"], data["start"])
        assert data["before"] == data["after"]
        
