from lesson2.lec.graph import Graph, Vertex, Edge
from lesson2.lab.dijkstra import dijkstra


def test_simple():
    almaty = Vertex("Almaty", 350, 400)
    karagandy = Vertex("Karagandy", 100, 70)
    astana = Vertex("Astana", 50, 50)
    balkhash = Vertex("Balkhash", 250, 250)
    shymkent = Vertex("Shymkent", 70, 450)
    london = Vertex("London", 1000, 1000)

    almaty_balkhash = Edge(almaty, balkhash, 500)
    balkhash_shymkent = Edge(balkhash, shymkent, 250)
    balkhash_karagandy = Edge(balkhash, karagandy, 500)
    karagandy_astana = Edge(karagandy, astana, 200)

    g = Graph()
    g.add_vertex(almaty)
    g.add_vertex(karagandy)
    g.add_vertex(astana)
    g.add_vertex(balkhash)
    g.add_vertex(shymkent)
    g.add_vertex(london)

    g.add_edge(almaty_balkhash)
    g.add_edge(balkhash_shymkent)
    g.add_edge(balkhash_karagandy)
    g.add_edge(karagandy_astana)

    dijkstra(g, almaty)
    assert almaty.dist == 0
    assert balkhash.dist == 500
    assert shymkent.dist == 750
    assert karagandy.dist == 1000
    assert astana.dist == 1200
    assert london.dist == float('inf')


def test_shorter():
    almaty = Vertex("Almaty", 350, 400)
    karagandy = Vertex("Karagandy", 100, 70)
    astana = Vertex("Astana", 50, 50)
    balkhash = Vertex("Balkhash", 250, 250)
    priozersk = Vertex("Priozersk", 220, 220)
    shymkent = Vertex("Shymkent", 70, 450)

    almaty_balkhash = Edge(almaty, balkhash, 500)
    balkhash_shymkent = Edge(balkhash, shymkent, 250)
    balkhash_karagandy = Edge(balkhash, karagandy, 500)
    balkhash_priozersk = Edge(balkhash, priozersk, 30)
    karagandy_astana = Edge(karagandy, astana, 200)

    priozersk_shymkent = Edge(priozersk, shymkent, 20)

    g = Graph()
    g.add_vertex(almaty)
    g.add_vertex(karagandy)
    g.add_vertex(astana)
    g.add_vertex(balkhash)
    g.add_vertex(shymkent)
    g.add_vertex(priozersk)

    g.add_edge(almaty_balkhash)
    g.add_edge(balkhash_shymkent)
    g.add_edge(balkhash_karagandy)
    g.add_edge(karagandy_astana)
    g.add_edge(balkhash_priozersk)
    g.add_edge(priozersk_shymkent)

    path = dijkstra(g, almaty, shymkent)
    assert almaty.dist == 0
    assert balkhash.dist == 500
    assert priozersk.dist == 530
    assert shymkent.dist == 550
    assert karagandy.dist == 1000
    assert astana.dist == float('inf')
    assert path == [almaty, balkhash, priozersk, shymkent]

    path = dijkstra(g, shymkent, almaty)
    assert path is None
