"""• Дана структура типа бинарное дерево. Все вершины
пронумерованы от 1 до n. Дерево задано в виде списка кортежей:
[(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]
• Каждый кортеж (a,b) показывает, что вершина a соединена с
вершиной b.
• По определению в дереве невозможны циклы.
• Найти максимальную длину от вершины (1) до конечной
вершины."""

tree = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)] #я пытался:(
s = {}


class Vertex:
    def __init__(self, parent, children):
        self.parent = parent
        self.children = children

    def __str__(self):
        return f" {self.parent} : {self.children}"

    def __repr__(self):
        return str(self.__dict__)

    def add_children(self, d):
        self.children.append(d)


def find_max(tree):
    if len(tree) != 0:
        vertex = tree.pop(0)
        if vertex[0] in s:
            s[vertex[0]].append(Vertex(vertex[0], vertex[1]))
        else:
            s[vertex[0]] = []
            s[vertex[0]].append(Vertex(vertex[0], vertex[1]))

        find_max(tree)


find_max(tree)

print(len(s))
