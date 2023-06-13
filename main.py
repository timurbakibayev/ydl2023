from graph import Graph, Vertex, Edge


def kazakhstan() -> Graph:
    # Canvas is 500 x 500 pixels
    # 0, 0 - top left
    # 500, 500 - bottom right

    almaty = Vertex("Almaty", 350, 400)
    karagandy = Vertex("Karagandy", 100, 70)
    astana = Vertex("Astana", 50, 50)
    balkhash = Vertex("Balkhash", 250, 250)
    shymkent = Vertex("Shymkent", 70, 450)

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

    g.add_edge(almaty_balkhash)
    g.add_edge(balkhash_shymkent)
    g.add_edge(balkhash_karagandy)
    g.add_edge(karagandy_astana)

    return g


def main():
    g = kazakhstan()
    g.save_to("kazakhstan.png")


if __name__ == '__main__':
    main()
