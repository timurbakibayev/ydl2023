from graph import Graph, Vertex, Edge


def kazakhstan() -> Graph:
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

    return g


def main():
    g = kazakhstan()
    g.save_to("kazakhstan.png")


if __name__ == '__main__':
    main()
