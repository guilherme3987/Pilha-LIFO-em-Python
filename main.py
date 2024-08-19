import tkinter as tk
from tkinter import messagebox

# Funções para manipular a pilha
pilha = []

def criando_pilha():
    global pilha
    pilha = []
    for x in range(10):
        pilha.append(x)
    pilha.sort(reverse=True)
    atualizar_pilha()

def operacoes_pilha():
    global pilha
    while len(pilha) > 1:
        dois_ultimos = pilha[-2:]
        penultimo = dois_ultimos[0]
        ultimo = dois_ultimos[1]
        soma = penultimo + ultimo
        pilha.pop()
        pilha.pop()
        pilha.append(soma)
    atualizar_pilha()

def atualizar_pilha():
    texto_pilha.set(f"Pilha Atual: {pilha}")

def criar_pilha():
    criando_pilha()
    messagebox.showinfo("Informação", "Pilha criada e ordenada.")

def operar_pilha():
    operacoes_pilha()
    messagebox.showinfo("Informação", "Operações realizadas na pilha.")

# Criar a interface gráfica
root = tk.Tk()
root.title("Interface da Pilha LIFO")
# Definir o tamanho fixo da janela
root.geometry("300x200")  # Largura x Altura

# Impedir redimensionamento da janela
root.resizable(False, False)
# Criar e organizar os widgets
texto_pilha = tk.StringVar()
texto_pilha.set("Pilha Atual: []")

label = tk.Label(root, textvariable=texto_pilha)
label.pack(pady=10)

botao_criar = tk.Button(root, text="Criar Pilha", command=criar_pilha)
botao_criar.pack(pady=5)

botao_operar = tk.Button(root, text="Operar Pilha", command=operar_pilha)
botao_operar.pack(pady=5)

# Inicializa a interface gráfica
root.mainloop()

'''
Adicionar operações clássas de uma pilha (como push, pop, peek, e verificar se a pilha está vazia)
'''