# Graph is Edges and Vertices
import random
from PIL import Image, ImageDraw


class Edge:
    def __init__(self, start: "Vertex", end: "Vertex", weight: int):
        self.start = start
        self.end = end
        self.weight = weight


class Vertex:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y
        self.edges = []
        self.id = random.randint(0, 10000)
        self.dist = None
        self.prev = None

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def __str__(self):
        return f"Vertex {self.name} at ({self.x}, {self.y})"

    def __lt__(self, other):
        return self.dist < other.dist


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, vertex: Vertex):
        self.vertices.append(vertex)

    def add_edge(self, edge: Edge):
        edge.start.add_edge(edge)

    def __str__(self):
        return f"Graph with {len(self.vertices)} vertices"

    def __repr__(self):
        return self.__str__()

    def save_to(self, filename: str):
        w = 20
        canvas = Image.new('RGB', (500, 500), color=(73, 109, 137))
        img = ImageDraw.Draw(canvas)
        for vertex in self.vertices:
            for edge in vertex.edges:
                img.line((edge.start.x, edge.start.y, edge.end.x, edge.end.y), fill=(255, 255, 255), width=2)
                center_x = (edge.start.x + edge.end.x) / 2
                center_y = (edge.start.y + edge.end.y) / 2
                img.text((center_x, center_y), str(edge.weight), fill=(25, 25, 25))

        for vertex in self.vertices:
            img.ellipse((vertex.x - w, vertex.y - w, vertex.x + w, vertex.y + w), fill=(255, 0, 0), outline=(0, 0, 0))
            img.text((vertex.x - w, vertex.y + w*1.1), vertex.name, fill=(255, 255, 255))

        canvas.save(filename)

