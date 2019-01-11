def g1(gen):
    yield from gen

def main():
    g=g1(range(4))
    g.send(None)

