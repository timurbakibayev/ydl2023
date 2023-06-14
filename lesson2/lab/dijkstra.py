from graph import Graph, Vertex, Edge
from typing import List, Union, Set, Dict


def mindistance(vertices: Set[Vertex]) -> Union[Vertex, None]:
    result = min(vertices)
    if result.dist == float("inf"):
        return None
    return result


def dijkstra(g: Graph, v_start: Vertex, v_end: Vertex = None) -> Union[List[Vertex], None]:
    """
    v_end we will only use to stop the algorithm earlier. If v_end is None then we will go on until Q is empty.
    :g:
    :param v_start:
    :param v_end:
    :return: list of vertices in the shortest path from v_start to v_end
    if there is no path from v_start to v_end then return None
    if v_end is None, return None
    """

    for vertex in g.vertices:
        if vertex == v_start:
            vertex.dist = 0
        else:
            vertex.dist = float("inf")

    q = set(g.vertices)
    while len(q) > 0:
        u = mindistance(q)
        if u is None:
            break
        q.remove(u)
        if u == v_end:
            break
        for edge in u.edges:
            v = edge.end
            if v.dist > u.dist + edge.weight:
                v.dist = u.dist + edge.weight
                v.prev = u

    if v_end is not None:
        if v_end in q:
            return None
        current = v_end
        result = [current]
        while current.prev is not None:
            current = current.prev
            result.insert(0, current)
        return result

    return None
