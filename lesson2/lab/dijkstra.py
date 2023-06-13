from lesson2.lec.graph import Graph, Vertex, Edge
from typing import List, Union


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
    ...
