import matplotlib.pyplot as plt
import networkx as nx
import pygraphviz
# Criando um grafo direcionado
G = nx.DiGraph()

# Adicionando nós ao grafo que representam as matérias do curso
matérias = [
    "Introdução à Computação",
    "Programação I",
    "Matemática Básica",
    "Lógica de Programação",
    "Estruturas de Dados",
    "Banco de Dados",
    "Programação II",
    "Matemática Discreta",
    "Algoritmos",
    "Redes de Computadores",
    "Sistemas Operacionais",
    "Engenharia de Software"
]

# Adicionando as matérias como nós no grafo
G.add_nodes_from(matérias)

# Adicionando as arestas que representam os pré-requisitos
pré_requisitos = [
    ("Introdução à Computação", "Programação I"),
    ("Introdução à Computação", "Lógica de Programação"),
    ("Matemática Básica", "Matemática Discreta"),
    ("Programação I", "Estruturas de Dados"),
    ("Programação I", "Programação II"),
    ("Lógica de Programação", "Algoritmos"),
    ("Estruturas de Dados", "Banco de Dados"),
    ("Estruturas de Dados", "Algoritmos"),
    ("Matemática Discreta", "Algoritmos"),
    ("Programação II", "Engenharia de Software"),
    ("Algoritmos", "Sistemas Operacionais"),
    ("Algoritmos", "Redes de Computadores")
]

# Adicionando as arestas ao grafo
G.add_edges_from(pré_requisitos)


pos = nx.nx_agraph.graphviz_layout(G, prog='dot')

# Desenhando o grafo com o novo layout
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, edge_color='k', linewidths=1, font_size=10, arrows=True)
plt.title('Gráfico Organizacional das Matérias de um Curso Genérico (Melhorado)')
plt.show()