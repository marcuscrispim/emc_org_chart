<<<<<<< Data
import tkinter as tk
from tkinter import messagebox
from data.disciplinas import disciplinas  # Importando o dicionário do novo arquivo

# Função para verificar quais disciplinas podem ser cursadas
def verificar_disciplinas():
    selecionadas = [disciplina for disciplina, var in disciplinas_vars.items() if var.get()]
    possiveis = []
    for disciplina, pre_requisitos in disciplinas.items():
        if all(pr in selecionadas for pr in pre_requisitos) and disciplina not in selecionadas:
            possiveis.append(disciplina)
    
    if possiveis:
        messagebox.showinfo("Disciplinas Possíveis", "\n".join(possiveis))
    else:
        messagebox.showinfo("Disciplinas Possíveis", "Nenhuma disciplina disponível para cursar.")

# Criação da interface gráfica
root = tk.Tk()
root.title("Verificação de Disciplinas")

# Adicionando instruções
tk.Label(root, text="Selecione as disciplinas que você já completou:").pack(anchor="w")

# Criação de um frame com barra de rolagem
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

# Criação de variáveis para cada disciplina
disciplinas_vars = {}
for disciplina in disciplinas.keys():
    var = tk.BooleanVar()
    tk.Checkbutton(scrollable_frame, text=disciplina, variable=var).pack(anchor="w")
    disciplinas_vars[disciplina] = var

canvas.pack(side="left", fill=tk.BOTH, expand=True)
scrollbar.pack(side="right", fill="y")

# Botão para verificar disciplinas
tk.Button(root, text="Verificar Disciplinas", command=verificar_disciplinas).pack()

root.mainloop()
=======
import matplotlib.pyplot as plt
import networkx as nx
import pygraphviz
# Criando um grafo direcionado
G = nx.DiGraph()

#testando branch

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
>>>>>>> main
